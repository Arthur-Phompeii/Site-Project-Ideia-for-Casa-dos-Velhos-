/* Carrega as preferências do usuário */
const botaoContraste = document.querySelector("#contraste");
botaoContraste.addEventListener("click", () => {

    document.documentElement.classList.toggle("alto-contraste");

    const ativado =
        document.documentElement.classList.contains("alto-contraste");

    localStorage.setItem(
        "altoContraste",
        ativado
    );
});

const botaoModoEscuro = document.querySelector("#modo-escuro");
botaoModoEscuro.addEventListener("click", () => {

    document.documentElement.classList.toggle("modo-escuro");

    const ativado =
        document.documentElement.classList.contains("modo-escuro");

    localStorage.setItem(
        "modoEscuro",
        ativado
    );
});

const movReduzido = document.querySelector("#movReduzido");
movReduzido.addEventListener("click", () => {

    document.documentElement.classList.toggle("movimento-reduzido");

    const ativado =
        document.documentElement.classList.contains("movimento-reduzido");

    localStorage.setItem(
        "movimentoReduzido",
        ativado
    );
});

const sliderFonte = document.querySelector("#slider-fonte");
sliderFonte.addEventListener("input", () => {
    const tamanhoFonte = sliderFonte.value;
    document.documentElement.style.fontSize = `${tamanhoFonte}px`;
    localStorage.setItem("tamanhoFonte", tamanhoFonte);
});

function getPreferences() {
    const altoContraste = localStorage.getItem("altoContraste");

    if (altoContraste === "true") {
        document.documentElement.classList.add("alto-contraste");
    }

    const modoEscuro = localStorage.getItem("modoEscuro");

    if (modoEscuro === "true") {
        document.documentElement.classList.add("modo-escuro");
    }

    const movimentoReduzido = localStorage.getItem("movimentoReduzido");

    if (movimentoReduzido === "true") {
        document.documentElement.classList.add("movimento-reduzido");
    }

    const tamanhoFonte = localStorage.getItem("tamanhoFonte");

    if (tamanhoFonte) {
        document.documentElement.classList.add(tamanhoFonte);
    }

}
getPreferences()

/* Guarda os dados do formulário para perda acidental */
const form = document.querySelector("#contact-form");

form.addEventListener("input", () => {

    const dados = {
        nome: form.nome.value,
        email: form.email.value,
        mensagem: form.mensagem.value
    };

    localStorage.setItem(
        "rascunhoContato",
        JSON.stringify(dados)
    );
});

function getDraft() {
    const rascunho =
        localStorage.getItem("rascunhoContato");

    if (rascunho) {
        const dados = JSON.parse(rascunho);

        form.nome.value = dados.nome;
        form.email.value = dados.email;
        form.mensagem.value = dados.mensagem;
    }
}
getDraft()

const submitButton = document.querySelector("#contact-form button[type='submit']");
submitButton.addEventListener("click", () => {
    localStorage.removeItem("rascunhoContato");
});