from django.shortcuts import render
from .dados import habilidades, projetos, contatos, links, sobre

def home(request):
    habilidades_nomes = [v['nome'] for v in habilidades.values()]
    return render(request, 'home.html', {'habilidades_js': habilidades_nomes, 'links': links})

def sobre_mim(request):
    return render(request, 'sobre_mim.html', {'habilidades': habilidades, 'contatos': contatos, 'links': links, 'sobre': sobre})

def lista_projetos(request):
    for projeto in projetos.values():
        if isinstance(projeto.get('tecnologia'), str):
            projeto['tecnologia'] = [t.strip() for t in projeto['tecnologia'].split(',')]
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projetos(request, id_projeto):
    projeto = projetos.get(id_projeto)
    if projeto and isinstance(projeto.get('tecnologia'), str):
        projeto['tecnologia'] = [t.strip() for t in projeto['tecnologia'].split(',')]
    return render(request, 'detalhes_projeto.html', {'projeto': projeto, 'links': links})




