import homeView from './views/home.js';
import projectsView from './views/projects.js';
import contactView from './views/contact.js';

const app = document.querySelector('#app');
const menuButton = document.querySelector('.menu-btn');
const header = document.querySelector('header');
const navigation = document.querySelector('.visibility');

lucide.createIcons();

/* Prepata os templates de HTML */
const views = {
    home: homeView,
    projects: projectsView,
    contact: contactView
};

const routes = {
    sobre: { view: 'home', anchor: 'app' },
    funcionamento: { view: 'home', anchor: 'funcionamento' },
    home: { view: 'home' },
    projects: { view: 'projects' },
    contact: { view: 'contact' }
};

let activeView;

/* Carrega um CSS específico */
/* function carregarCSS(nome) {
    const id = `css-${nome}`;

    if (document.getElementById(id)) {
        return;
    }

    const link = document.createElement("link");

    link.id = id;
    link.rel = "stylesheet";
    link.href = `./assets/css/${nome}.css`;

    document.head.appendChild(link);
} */
const estilos = {
    home: () => import("../css/home.css"),
    contact: () => import("../css/contact.css"),
    projects: () => import("../css/projects.css")
};

async function carregarCSS(nome) {
    if (!estilos[nome]) {
        throw new Error(`CSS "${nome}" não encontrado.`);
    }

    await estilos[nome]();
}

/* Configura o formulário de contato */
function setupContactForm() {
    /* Encontra o Formulário no HTML */
    const form = document.querySelector('#contact-form');
    
    /* Valida a existência do formulário */
    if (!form) {
        return;
    }

    const telefone = document.querySelector("#celular");
    
    const mascara = IMask(telefone, {
        mask: "(00) 00000-0000"
    });
    
    /* Função genérica para mensagem de erro */
     function mostrarErro(campo, mensagem) {
        const container = campo.parentElement;

        let erro = container.querySelector('.campo__erro');

        if (!erro) {
            erro = document.createElement('small');
            erro.className = 'campo__erro';
            container.append(erro);
        }

        erro.textContent = mensagem;
        
        container.classList.add('invalido');
        container.classList.remove('valido');
        
        erro.id = `erro-${campo.id}`;

        campo.setAttribute('aria-describedby', erro.id);
        campo.setAttribute('aria-invalid', 'true');
    }

    /* Função que retira mensagem de erro */
    function removerErro(campo) {
        const container = campo.parentElement;
        const erro = container.querySelector('.campo__erro');

        container.classList.remove('invalido');
        campo.removeAttribute('aria-describedby');
        campo.removeAttribute('aria-invalid');
        container.classList.add('valido');

        if (erro) {
            erro.remove();
        }

        campo.setAttribute('aria-invalid', 'false');
    }

    /* Designação de mensagens e ações*/
    function validarCampo(campo) {

        if (campo.validity.valid) {
            removerErro(campo);
            return true;
        }

        if (campo.validity.valueMissing) {
            mostrarErro(campo.parentElement.parentElement, 'Este campo é obrigatório.');
        }

        else if (campo.validity.typeMismatch) {
            mostrarErro(campo, 'Digite um e-mail válido.');
        }

        else if (campo.validity.tooShort) {
            mostrarErro(
                campo,
                `Digite pelo menos ${campo.minLength} caracteres.`
            );
        }
        
        return false;
    }

    /* Validação do Campo em tempo real */
    const campos = form.querySelectorAll('input, select, textarea');

    campos.forEach(campo => {
        
        let foiValidado = false;
        console.log("oi");

        campo.addEventListener('blur', () => {
            foiValidado = true;
            validarCampo(campo);
        });

        campo.addEventListener('input', () => {
            if (foiValidado) {
                validarCampo(campo);
            }
        });

    });

    /* Trata do envio do formulário */
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        /* Faz uma verificação dos campos antes do envio do formulário */
        let formularioValido = true;

        campos.forEach(campo => {
            const valido = validarCampo(campo);

            if (!valido) {
                formularioValido = false;
            }
        });

        if (!formularioValido) {
            return;
        }

        let status = document.querySelector('#form-status');
        if (!status) {
            status = document.createElement('p');
            status.id = 'form-status';
            status.setAttribute('role', 'status');
            status.setAttribute('aria-live', 'polite');
            form.append(status);
        }
        status.textContent = 'Obrigado! Sua solicitação foi registrada. Entraremos em contato em breve.';
        form.reset();
    });
}

function navigate() {
    /* Encontra a URL alvo */
    const target = window.location.hash.slice(1) || 'sobre';
    /* Traduz o alvo para o comportamento desejado */
    const route = routes[target] || routes.sobre;

    /* Renderiza a view se ela já não estiver renderizada */
    if (activeView !== route.view) {
        carregarCSS(route.view);
        app.innerHTML = views[route.view];
        activeView = route.view;
        setupContactForm();
    }

    /* Identifica se existe necessidade de rolar para um elemento específico */
    if (route.anchor) {
        document.getElementById(route.anchor)?.scrollIntoView({ behavior: 'smooth' });
    } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    /* Fecha o menu se estiver aberto */
    header.classList.remove('show-menu');
    menuButton?.setAttribute('aria-expanded', 'false');
}

window.addEventListener('hashchange', navigate);
navigate();

menuButton?.addEventListener('click', () => {
    const isOpen = header.classList.toggle('show-menu');
    menuButton.setAttribute('aria-expanded', String(isOpen));
});

navigation?.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
        header.classList.remove('show-menu');
        menuButton?.setAttribute('aria-expanded', 'false');
    }
});