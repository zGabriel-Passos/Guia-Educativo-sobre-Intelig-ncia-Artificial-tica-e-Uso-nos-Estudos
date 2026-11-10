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

# Itens da navbar: (seção, rótulo)
NAV = [
    ("estudos", "Uso nos estudos"),
    ("etica-direitos", "Ética e direitos"),
    ("desinformacao", "Desinformação"),
    ("ciberseguranca", "Segurança"),
    ("quiz", "Quiz"),
    ("mural", "Comunidade"),
]


@app.context_processor
def inject_nav():
    return {"nav": NAV}


@app.after_request
def security_headers(resp):
    resp.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; "
        "script-src 'self' https://www.gstatic.com https://apis.google.com; "
        "connect-src 'self' https://*.googleapis.com https://*.firebaseio.com https://identitytoolkit.googleapis.com https://securetoken.googleapis.com; "
        "img-src 'self' data:; frame-src https://*.firebaseapp.com https://accounts.google.com; "
        "frame-ancestors 'none'; base-uri 'self'; form-action 'self'"
    )
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    resp.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return resp


@app.get("/")
def home():
    return render_template("home.html", paginas=PAGINAS)


@app.get("/<slug>")
def conteudo(slug):
    if slug not in PAGINAS:
        abort(404)
    return render_template("pagina.html", pagina=PAGINAS[slug])


@app.get("/quiz")
def quiz():
    return render_template("quiz.html")


@app.get("/mural")
def mural():
    return render_template("mural.html")


@app.get("/entrar")
def entrar():
    return render_template("entrar.html")


@app.errorhandler(404)
def nao_encontrada(_):
    return render_template("em_breve.html", titulo="Página não encontrada",
                           texto="Esse endereço não existe. Use o menu para voltar."), 404


if __name__ == "__main__":
    app.run(debug=True)
