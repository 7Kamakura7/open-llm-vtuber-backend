import os
import uvicorn
from src.open_llm_vtuber.server import WebSocketServer

# ==========================
# Variables de entorno
# ==========================

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Opcionales ya definidos en código:
HF_HOME = os.getenv("HF_HOME", "/root/.cache/huggingface")
MODELSCOPE_CACHE = os.getenv("MODELSCOPE_CACHE", "/root/.cache/modelscope")
HF_ENDPOINT = os.getenv("HF_ENDPOINT")  # opcional

# ==========================
# Main
# ==========================

if __name__ == "__main__":
    # ⚠️ check_frontend_submodule() deshabilitado porque el frontend se sirve desde Cloudflare Pages
    # check_frontend_submodule()

    host = "0.0.0.0"
    port = int(os.getenv("PORT", 8080))  # Cloud Run inyecta PORT automáticamente

    server = WebSocketServer()
    uvicorn.run(server.app, host=host, port=port)
