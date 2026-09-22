export default String.raw`<section class="about">
            <div class="text-decoration">
                <img src="./assets/images/text_decoration.avif" alt="Decoração textual em formato de coração.">
                <h1>Informações de Contato e Localização</h1>
            </div>
            <p>Se você quiser saber mais sobre a instituição ou fazer uma doação, entre em contato conosco através das informações abaixo:</p>
            <div class="contact-group">
                <div class="map">
                    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d7322.238724413749!2d-46.37963200000001!3d-23.420055!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce8821c2144f19%3A0xe399de56539c2e68!2sCasa%20dos%20Velhos%20Irm%C3%A3%20Alice!5e0!3m2!1spt-BR!2sus!4v1788637020337!5m2!1spt-BR!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
                </div>
                <div class="contact-info">
                    <h2>Endereço</h2>
                    <p>Av. Ladslau Kardos, 94 – (KM 206 Rodovia Presidente Dutra -sentido Rio de Janeiro)
                    <br>Bairro: Cidade Aracilia – Guarulhos/SP</p>
                    <h2>Telefones</h2>
                    <p>(011) 2480-4566 | (011) 2480-0508 </p>
                    <h2>E-mail</h2>
                    <p>Administrativo: adm@casadosvelhos.org.br
                    <br>Contatos: ajude@casadosvelhos.org.br</p>
                    <h2>Horário de visita:</h2>
                    <p>Preferencialmente aos Sábados – das 13h as 16h</p>
                    <h2>Atendimento ao público</h2>
                    <p>O atendimento ao público - das 8:00 h e 17:00 h.</p>
                </div>
            </div>
            <div class="warning">
                <h3>Aviso!</h3>
                <h4>Eventos e atividades em grupos</h4>
                <p>As visitas com a finalidade de promover festas, lanches, cultos religiosos ou outras atividades lúdicas, necessitarão de autorização prévia da diretoria. Para isso basta preencher o formulário de solicitação disponível na aba abaixo para entrarmos em contato com os detalhes.</p>
            </div>
        </section>
        <section class="about">
            <div class="text-decoration">
                <img src="./assets/images/text_decoration.avif" alt="Decoração textual em formato de coração.">
                <h1>Envio de Solicitação de Contato</h1>
            </div>
            <p>Para a realização de algumas atividades, solicitação de acolhimento de idoso, voluntariado, pedimos que entrem em contato conosco através do formulário abaixo. Basta selecionar a opção correspondente e preencher os dados solicitados.</p>
            <div class="form-container">
                <form>
                    <fieldset>
                        <legend for="categoria">Categoria</legend>
                        <div class="radio-group">
                            <label class="radio">
                                <input type="radio" name="categoria" value="acolhimento" required> Internação
                            </label>
                            <label class="radio">
                                <input type="radio" name="categoria" value="voluntariado" required> Voluntariado
                            </label>
                            <label class="radio">
                                <input type="radio" name="categoria" value="doacoes" required> Doações
                            </label>
                            <label class="radio">
                                <input type="radio" name="categoria" value="eventos" required> Eventos
                            </label>
                        </div>
                    </fieldset>
                    
                    <div class="user-info">
                        <fieldset>
                            <legend>Informações de Contato</legend>
                            <div class="contact-info-form">
                                <div class="campo">
                                    <label for="nome">Nome:</label>
                                    <input type="text" id="nome" name="nome" placeholder="Digite seu nome" required>
                                </div>
                                <div class="campo">
                                    <label for="celular">Celular:</label>
                                    <input type="tel" id="celular" name="celular" placeholder="(00) 00000-0000" inputmode="tel" autocomplete="tel" maxlength="11" pattern="[0-9]{11}" required>
                                </div>
                                <div class="campo">
                                    <label for="email">E-mail:</label>
                                    <input type="email" id="email" name="email" placeholder="Digite seu e-mail" inputmode="email" autocomplete="email" required>
                                </div>
                            </div>
                        </fieldset>
                    </div>
    
                    <fieldset>
                        <legend>Mensagem</legend>
                        <div class="message">
                            <label for="mensagem">Deixe aqui sua mensagem:</label>
                            <textarea id="mensagem" name="mensagem" rows="4" placeholder="Digite sua mensagem" required></textarea>
                        </div>
                    </fieldset>
    
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </section>`;
