links = {
        'linkedin': 'http://www.linkedin.com/in/matheus-de-paula-291947187',
        'github': 'https://github.com/MatheusPaula02',
        'email': 'paulaemanuel009@gmail.com',
        'imagem_port': {
            'imagem_bi': {
                'avaliacao.png',
                'personificacao.jpg',
                'principal.png'
            },
            'imagem_excel': {
                'formulario.png',
                'dashboard.png',
            },
            'imagem_portf': {
                'home.png',
                'sobre.png',
                'projetos.png',
                'detalhes.png',
            },
        },
}

contatos = ({
        'icone': 'email_icon.html',
        'texto': links['email']
    },
    {
        'icone': 'whatsapp_icon.html',
        'texto': '+55 19 99122-6113'
    },
)

sobre = {
    'descricao': (
        'Sou formado em Ciência da Computação e tenho experiência no tratamento, '
        'análise e visualização de dados para apoiar decisões estratégicas e otimizar processos. '
        'Iniciei minha carreira na área de Logística, atuando na consolidação de históricos e '
        'criação de relatórios e dashboards em Excel (com VBA), transformando dados operacionais '
        'em insights que auxiliaram na prevenção de riscos e melhoria de desempenho.\n\n'

        'Atualmente, trabalho com análise e otimização de queries SQL voltadas ao tratamento de '
        'dados fiscais (SPED), garantindo precisão e conformidade das informações. Também desenvolvo '
        'scripts em Python e automações com Power Automate, que reduziram significativamente o tempo '
        'de atendimento e aumentaram a eficiência de processos internos. Além disso, crio views e '
        'relatórios dinâmicos em SQL Server, traduzindo dados complexos em informações claras para '
        'clientes e equipes de negócio.\n\n'

        'Sou movido pelo desafio de transformar dados em decisões práticas, buscando constantemente '
        'aprimorar meus conhecimentos em Data Analytics, ETL/ELT e visualização de dados para continuar '
        'evoluindo na área e gerar impacto real por meio da informação.'
    )
}

habilidades = {
    'habilidade1': {
        'nome': 'Python',
        'emoji': '🐍'
    },
    'habilidade2': {
        'nome': 'SQL Server',
        'emoji': '🛢'
    },
    'habilidade3': {
        'nome': 'Excel',
        'emoji': '📊'
    },
    'habilidade4': {
        'nome': 'Power BI',
        'emoji': '📶'
    },
    'habilidade5': {
        'nome': 'Automação de processos (Power Automate)',
        'emoji': '⚙️'
    },
    'habilidade6': {
        'nome': 'Modelagem / Tratamento de Dados',
        'emoji': '🧩'
    },
    'habilidade7': {
        'nome': 'ETL / ELT',
        'emoji': '🔄'
    },
}

projetos = {
    'projeto1': {
        'título': 'Scripts SQL Desenvolvidos',
        'descricao': 'Conjunto de scripts SQL desenvolvidos para estudo, automação, análise de dados e implementação em clientes.',
        'tecnologia': 'SQL Server',
        'github': 'https://github.com/MatheusPaula02/SQL_Scripts.git',
        'funcionalidades': (
            'Manipulação e tratamento de dados utilizando SELECT, JOIN, UNION, CASE, CTE e Window Functions;',
            'Aplicação de boas práticas e técnicas de otimização de queries para ganho de performance;',
            'Execução de cálculos fiscais, cruzamentos de informações e análises comparativas.'
        ),
        'sobre':
            'Este repositório reúne uma coleção de scripts SQL desenvolvidos para estudo, automação de processos '
            'e análise de dados, com foco na otimização de consultas, integridade das informações e boas práticas '
            'de modelagem. Os exemplos abrangem desde rotinas de ETL e tratamento de dados até consultas analíticas, '
            'criação de relatórios e auditorias de consistência, refletindo situações que ocorrem em ambientes '
            'corporativos reais.\n\n'

            'Cada caso foi elaborado com base em cenários inspirados em experiências reais de projetos e demandas de '
            'clientes, além de processos contínuos de estudo e aprimoramento. Todos os exemplos foram testados, ajustados '
            'e otimizados ao longo do tempo, refletindo situações práticas enfrentadas no dia a dia profissional.\n\n'

            'Todos os scripts foram testados em SQL Server, mas podem ser facilmente adaptados para outros bancos '
            'de dados relacionais, como PostgreSQL e MySQL.',
    },
    'projeto2': {
        'título': 'Dashboards - Power BI',
        'descricao': 'Dashboards desenvolvidos no Power BI para transformar dados brutos em insights claros e acionáveis.',
        'tecnologia': ('Power BI','DAX'),
        'github': 'https://github.com/MatheusPaula02/PowerBI_Portfolio.git',
        'funcionalidades': (
            'Desenvolvimento de medidas e KPIs personalizados utilizando DAX;',
            'Utilização de Power Query para tratamento, limpeza e transformação dos dados;',
            'Implementação de filtros dinâmicos, segmentações e navegação por botões;',
            'Aplicação de boas práticas de design, cores e hierarquia visual.'
        ),
        'imagem': links['imagem_port']['imagem_bi'],
        'sobre':
            'Este repositório apresenta dashboards e relatórios desenvolvidos no Power BI, com foco em análise de '
            'desempenho, monitoramento de indicadores e apoio à tomada de decisão.\n\n'

            'Os projetos envolvem integração, modelagem e aplicação de DAX para criação de métricas e cálculos '
            'personalizados, apresentando boas práticas de design e visualização.\n\n'

            'Cada dashboard foi elaborado com base em fontes de dados reais ou fictícias, demonstrando como dados '
            'podem se transformar em insights estratégicos.'
        ,
    },
        'projeto3': {
        'título': 'Controle Cantoneiras - Dashboard (Excel VBA)',
        'descricao': 'Dashboard interativo em Excel VBA para controle de cantoneiras, com formulário automatizado para registro e atualização dos dados.',
        'tecnologia': ('Excel','VBA'),
        'github': 'https://github.com/MatheusPaula02/excel_vba_dashboard.git',
        'funcionalidades': (
            'Processamento Automatizado via VBA: Ao confirmar o envio, o sistema grava as informações na planilha e atualiza automaticamente todos os relatórios, gráficos e indicadores;',
            'Dashboard Inteligente e Dinâmica: Painel visual conectado às Tabelas Dinâmicas e Gráficos Dinâmicos, permitindo análise instantânea;',
            'Formulário Interativo de Entrada: Interface intuitiva para o usuário inserir dados.'
        ),
        'imagem': links['imagem_port']['imagem_excel'],
        'sobre':
            'Projeto desenvolvido durante minha atuação como Jovem Aprendiz de Logística, com o objetivo de automatizar '
            'o registro e análise de dados operacionais no Excel.\n\n'

            'A solução, criada em VBA, permite o preenchimento de informações por meio de um formulário interativo e atualiza '
            'automaticamente uma dashboard com gráficos e indicadores de desempenho.'

        ,
    },
        'projeto4': {
        'título': 'Portfólio Pessoal - WEB',
        'descricao': 'Portfólio criado para publicação de projetos e saber um pouco mais sobre mim.',
        'tecnologia': ('HTML','Python','CSS','JavaScript'),
        'github': 'https://github.com/MatheusPaula02/portfolio_web.git',
        'funcionalidades': (
            'Apresentação Pessoal: Seção que destaca minha trajetória e principais habilidades técnicas;',
            'Portfólio de Projetos: Galeria com descrições e links para código e detalhes;',
            'Área para entrar em contato (Email, Linkedin, Github), e com a possibilidade de download do meu currículo.',
        ),
        'imagem': links['imagem_port']['imagem_portf'],
        'sobre':
            'Este portfólio é uma representação visual e funcional das minhas habilidades e experiências, onde '
            'publicarei todos os projetos voltados a Análise/Ciências/Engenharia de dados que estarei desenvolvendo.\n\n' 

            'Sinta-se à vontade para explorar, conhecer meus projetos e entrar em contato para oportunidades.'
        ,
    },

}


