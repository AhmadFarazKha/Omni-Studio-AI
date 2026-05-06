import sys
import os
import gradio as gr
from dotenv import load_dotenv

# ── Path setup: allow imports from project root ───────────────────────────────
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from tools.story_gen import generate_multilingual_story

# Load .env from project root
load_dotenv(os.path.join(BASE_DIR, ".env"))
GEMINI_KEY = os.getenv("GOOGLE_API_KEY", "")

# ── Core processing function ──────────────────────────────────────────────────
def process(prompt: str, lang: str):
    """Called by Gradio on button click."""
    if not prompt or not prompt.strip():
        return "⚠️ Please enter a topic before generating.", []

    script = generate_multilingual_story(prompt.strip(), lang, GEMINI_KEY)
    return script, []   # Gallery left empty; add image URLs here if needed


# ── UI Layout ─────────────────────────────────────────────────────────────────
with gr.Blocks(theme=gr.themes.Soft(), title="Omni Studio AI") as demo:
    gr.Markdown("## 🎙️ Omni Studio AI — Multilingual Script Generator")
    gr.Markdown("Enter a topic, choose a language, and get a 50-second spoken script instantly.")

    with gr.Row():
        with gr.Column(scale=1):
            prompt_box = gr.Textbox(
                label="Topic / Prompt",
                placeholder="e.g. A robot learning to cook Pakistani food",
                lines=3,
            )
            lang_drop = gr.Dropdown(
                choices=["English", "Urdu", "Hindi"],
                label="Output Language",
                value="Urdu",
            )
            generate_btn = gr.Button("⚡ Generate Script", variant="primary")

        with gr.Column(scale=1):
            output_box = gr.TextArea(
                label="Generated Script",
                lines=14,
            )

    gallery = gr.Gallery(label="Concept Images", visible=False)  # hidden until images are provided

    generate_btn.click(
        fn=process,
        inputs=[prompt_box, lang_drop],
        outputs=[output_box, gallery],
    )

# ── Launch ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo.launch(
        server_port=7860,
        server_name="0.0.0.0",   # accessible on local network
        share=False,             # set True to get a public Gradio link
    )