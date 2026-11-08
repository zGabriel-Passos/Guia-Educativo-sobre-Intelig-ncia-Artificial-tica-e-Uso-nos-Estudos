import os

from dotenv import load_dotenv
from flask import Flask, abort, render_template

from data.conteudo import PAGINAS

load_dotenv()

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev-apenas-local"),
    SESSION_COOKIE_SECURE=os.environ.get("VERCEL") is not None,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

# Itens da navbar: (rota, rótulo)
NAV = [
    ("/estudos", "Uso nos estudos"),
    ("/etica-direitos", "Ética e direitos"),
    ("/desinformacao", "Deepfakes"),
    ("/ciberseguranca", "Cibersegurança"),
    ("/quiz", "Quiz"),
    ("/mural", "Comunidade"),
]


@app.context_processor
def inject_nav():
    return {"nav": NAV}


@app.after_request
def security_headers(resp):
    # Ao adicionar o Firebase (fase 2), liberar os domínios dele no CSP.
    resp.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; "
        "script-src 'self'; img-src 'self' data:; "
        "frame-ancestors 'none'; base-uri 'self'; form-action 'self'"
    )
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    resp.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return resp


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/<slug>")
def conteudo(slug):
    pagina = PAGINAS.get(slug)
    if not pagina:
        abort(404)
    return render_template("pagina.html", pagina=pagina)


@app.get("/quiz")
def quiz():
    return render_template("em_breve.html", titulo="Quiz",
                           texto="O quiz chega na próxima fase. Enquanto isso, leia os guias.")


@app.get("/mural")
def mural():
    return render_template("em_breve.html", titulo="Comunidade",
                           texto="O mural chega na próxima fase, junto com o login.")


@app.get("/entrar")
def entrar():
    return render_template("em_breve.html", titulo="Entrar",
                           texto="O login com Firebase Auth chega na próxima fase.")


@app.errorhandler(404)
def nao_encontrada(_):
    return render_template("em_breve.html", titulo="Página não encontrada",
                           texto="Esse endereço não existe. Use o menu para voltar."), 404


if __name__ == "__main__":
    app.run(debug=True)
