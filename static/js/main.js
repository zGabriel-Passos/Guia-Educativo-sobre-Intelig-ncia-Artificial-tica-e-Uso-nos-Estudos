// Menu mobile
const btn = document.getElementById("menuBtn");
const links = document.getElementById("navLinks");
if (btn && links) {
  btn.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    btn.setAttribute("aria-expanded", String(open));
  });

  links.querySelectorAll('a').forEach((link) => {
    link.addEventListener("click", () => {
      links.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    });
  });
}

const questions = [
  { q: "Usar IA para organizar ideias e depois escrever com suas palavras é…", a: ["Uso ético", "Plágio automático", "Sempre proibido"], correct: 0, info: "A ferramenta pode apoiar o processo; a compreensão e a autoria continuam sendo suas." },
  { q: "Uma referência indicada por uma IA deve ser…", a: ["Usada sem conferir", "Verificada na fonte original", "Copiada no trabalho"], correct: 1, info: "Modelos podem inventar autores, livros, links e dados. Sempre confira." },
  { q: "Uma mensagem urgente com voz de alguém conhecido pedindo PIX pede…", a: ["Envio imediato", "Confirmação por outro canal", "Compartilhamento"], correct: 1, info: "Vozes podem ser clonadas. Ligue ou confirme pelo contato que você já conhece." },
  { q: "Ter acesso ao código de um site significa poder copiá-lo?", a: ["Sim", "Não", "Só se mudar as cores"], correct: 1, info: "Código acessível não é sinônimo de código livre. Respeite licenças e autoria." }
];
const quiz = document.querySelector("#quiz");
if (quiz) {
  let index = 0, score = 0;
  const progress = document.querySelector("#quizProgress"), question = document.querySelector("#quizQuestion"), answers = document.querySelector("#quizAnswers"), feedback = document.querySelector("#quizFeedback"), next = document.querySelector("#nextQuestion");
  const render = () => {
    const item = questions[index]; progress.textContent = `PERGUNTA ${index + 1} DE ${questions.length}`; question.textContent = item.q; answers.innerHTML = ""; feedback.hidden = true; next.hidden = true;
    item.a.forEach((answer, i) => {
      const label = document.createElement("label"); label.className = "answer"; label.innerHTML = `<input type="radio" name="answer" value="${i}"><span></span>`; label.querySelector("span").textContent = answer; label.addEventListener("change", () => {
        const ok = i === item.correct; if (ok) score += 1; answers.querySelectorAll("input").forEach(input => input.disabled = true); feedback.textContent = `${ok ? "Resposta correta." : "Quase."} ${item.info}`; feedback.hidden = false; next.hidden = false;
      }); answers.append(label);
    });
  };
  next.addEventListener("click", () => { index += 1; if (index < questions.length) render(); else { progress.textContent = "RESULTADO"; question.textContent = `${score} de ${questions.length} respostas corretas.`; answers.innerHTML = ""; feedback.textContent = score >= 3 ? "Você está no caminho certo: continue verificando fontes e respeitando a autoria." : "Vale revisitar os guias: decisões responsáveis começam pela informação."; feedback.hidden = false; next.hidden = true; } });
  render();
}

const themeToggle = document.querySelector("#themeToggle");
const savedTheme = localStorage.getItem("guia-theme");
const applyTheme = (theme) => {
  const dark = theme === "dark";
  document.body.classList.toggle("theme-dark", dark);
  if (themeToggle) {
    themeToggle.setAttribute("aria-pressed", String(dark));
    themeToggle.setAttribute("aria-label", dark ? "Ativar tema claro" : "Ativar tema escuro");
    themeToggle.querySelector("span").textContent = dark ? "☾" : "☀";
  }
};
applyTheme(savedTheme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));
if (themeToggle) themeToggle.addEventListener("click", () => {
  const next = document.body.classList.contains("theme-dark") ? "light" : "dark";
  localStorage.setItem("guia-theme", next);
  applyTheme(next);
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
