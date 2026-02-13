from fpdf import FPDF

# Caminho das imagens de fundo (uma por página)
background_images = [
    'fundo_capa.png',
    'fundo_quem_somos.png',
    'fundo_servicos_gestao.png',
    'fundo_servicos_avulsos.png',
    'fundo_redes_sociais.png',
    'fundo_beneficios.png',
    'fundo_precos.png',
    'fundo_proximo_passo.png'
]

# Criar PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=True, margin=15)

# Dados de cada página
pages = [
    {'title': 'NexSupport.TI', 'text': 'Sua empresa não para. Nós monitoramos e protegemos sua TI remotamente.',
     'whatsapp': False, 'instagram': False},
    {'title': 'Quem Somos',
     'text': 'Empresa especializada em gestão remota de TI e marketing digital. Garantimos que seus sistemas funcionem 24h por dia e ajudamos a aumentar sua presença online.',
     'whatsapp': False, 'instagram': False},
    {'title': 'Serviços - Gestão Remota',
     'text': 'Monitoramento de PCs e servidores\nBackup e segurança de dados\nSuporte remoto rápido\nManutenção preventiva',
     'whatsapp': False, 'instagram': False},
    {'title': 'Serviços Avulsos',
     'text': 'Instalação de sistemas e servidores\nFormatação e recuperação de dados\nLimpeza de vírus e malwares\nConfiguração de rede e impressoras\nDiagnóstico remoto gratuito',
     'whatsapp': False, 'instagram': False},
    {'title': 'Gestão de Redes Sociais',
     'text': 'Criação de conteúdo (posts, reels, stories)\nAutomação de mensagens e atendimento\nAumento da presença digital da empresa',
     'whatsapp': True, 'instagram': True},
    {'title': 'Benefícios',
     'text': 'Evita paradas e prejuízos\nSuporte remoto rápido\nRelatórios mensais de TI e desempenho digital\nDiagnóstico inicial gratuito e sem compromisso\nTudo gerenciado por uma única empresa confiável',
     'whatsapp': False, 'instagram': False},
    {'title': 'Preços',
     'text': 'MSP remoto (PCs + servidor): a partir de R$ 497/mês\nServiços avulsos: R$ 80-R$ 250 por atendimento\nRedes sociais: R$ 497-R$ 997/mês\n\nExemplo completo: 10 PCs + 1 servidor = R$ 787/mês\nGestão de redes sociais = R$ 497/mês\nTotal mensal: R$ 1.284',
     'whatsapp': False, 'instagram': False},
    {'title': 'Próximo Passo',
     'text': 'Agende seu diagnóstico remoto gratuito. Avaliamos sua TI e presença digital e apresentamos soluções completas para proteger e fazer sua empresa crescer.',
     'whatsapp': True, 'instagram': True}
]

# Criar páginas
for i, page in enumerate(pages):
    pdf.add_page()
    # Adicionar imagem de fundo
    pdf.image(background_images[i], x=0, y=0, w=210, h=297)

    # Adicionar título
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_text_color(255, 255, 255)  # branco sobre a imagem
    pdf.cell(0, 10, page['title'], ln=True, align='C')
    pdf.ln(10)

    # Adicionar texto
    pdf.set_font('helvetica', '', 14)
    pdf.multi_cell(0, 8, page['text'])
    pdf.ln(10)

    # Links clicáveis se houver
    pdf.set_text_color(0, 102, 204)  # azul
    pdf.set_font('helvetica', 'U', 14)
    if page['whatsapp']:
        pdf.cell(0, 10, 'WhatsApp: Clique aqui', ln=True, link='https://wa.me/5515996999011')
    if page['instagram']:
        pdf.cell(0, 10, 'Instagram: @NexSupport.TI', ln=True, link='https://instagram.com/NexSupport.TI')
    pdf.set_text_color(255, 255, 255)  # reset cor para branco para próximas páginas

# Salvar PDF
pdf.output('/mnt/data/NexSupport_TI_Final_Com_Links.pdf')
