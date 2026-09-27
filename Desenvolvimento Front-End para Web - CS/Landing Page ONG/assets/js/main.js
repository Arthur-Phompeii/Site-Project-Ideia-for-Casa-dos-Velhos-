import homeView from './views/home.js';
import projectsView from './views/projects.js';
import contactView from './views/contact.js';

const app = document.querySelector('#app');
const menuButton = document.querySelector('.menu-btn');
const header = document.querySelector('header');
const navigation = document.querySelector('.visibility');

const views = {
    home: homeView,
    projects: projectsView,
    contact: contactView
};

const routes = {
    sobre: { view: 'home', anchor: 'presentation' },
    funcionamento: { view: 'home', anchor: 'funcionamento' },
    home: { view: 'home' },
    projetos: { view: 'projects' },
    contato: { view: 'contact' }
};

let activeView;

function setupContactForm() {
    const form = document.querySelector('#contact-form');
    if (!form) {
        return;
    }

    form.addEventListener('submit', (event) => {
        event.preventDefault();
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
    const target = window.location.hash.slice(1) || 'sobre';
    const route = routes[target] || routes.sobre;

    if (activeView !== route.view) {
        app.innerHTML = views[route.view];
        activeView = route.view;
        setupContactForm();
    }

    if (route.anchor) {
        document.getElementById(route.anchor)?.scrollIntoView({ behavior: 'smooth' });
    } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

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
