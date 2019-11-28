from gulosos.Cidade import Cidade
from gulosos.Adjacente import Adjacente

class Mapa:
    portoUniao = Cidade("Porto União", 203)
    pauloFrontin = Cidade("Paulo Frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    irati = Cidade("Irati", 139)
    palmeira = Cidade("Palmeira", 59)
    campoLargo = Cidade("Campo Largo", 27)
    curitiba = Cidade("Curitiba", 0)
    balsaNova = Cidade("Balsa Nova", 41)
    araucaria = Cidade("Araucária", 23)
    saoJose = Cidade("São José dos Pinhais", 13)
    contenda = Cidade("Contenda", 39)
    mafra = Cidade("Mafra", 94)
    tijucas = Cidade("Tijucas do Sul", 56)
    lapa = Cidade("Lapa", 74)
    saoMateus = Cidade("São Mateus do Sul", 123)
    tresBarras = Cidade("Três Barras", 131)
    
    portoUniao.addCidadeAdjacentes(Adjacente(pauloFrontin))
    portoUniao.addCidadeAdjacentes(Adjacente(canoinhas))
    portoUniao.addCidadeAdjacentes(Adjacente(saoMateus))
    
    pauloFrontin.addCidadeAdjacentes(Adjacente(portoUniao))
    pauloFrontin.addCidadeAdjacentes(Adjacente(irati))
    
    canoinhas.addCidadeAdjacentes(Adjacente(portoUniao))
    canoinhas.addCidadeAdjacentes(Adjacente(tresBarras))
    canoinhas.addCidadeAdjacentes(Adjacente(mafra))
    
    irati.addCidadeAdjacentes(Adjacente(pauloFrontin))
    irati.addCidadeAdjacentes(Adjacente(palmeira))
    irati.addCidadeAdjacentes(Adjacente(saoMateus))
    
    palmeira.addCidadeAdjacentes(Adjacente(irati))
    palmeira.addCidadeAdjacentes(Adjacente(saoMateus))
    palmeira.addCidadeAdjacentes(Adjacente(campoLargo))

    campoLargo.addCidadeAdjacentes(Adjacente(palmeira))
    campoLargo.addCidadeAdjacentes(Adjacente(balsaNova))
    campoLargo.addCidadeAdjacentes(Adjacente(curitiba))
    
    curitiba.addCidadeAdjacentes(Adjacente(campoLargo))
    curitiba.addCidadeAdjacentes(Adjacente(balsaNova))
    curitiba.addCidadeAdjacentes(Adjacente(araucaria))
    curitiba.addCidadeAdjacentes(Adjacente(saoJose))
    
    balsaNova.addCidadeAdjacentes(Adjacente(curitiba))
    balsaNova.addCidadeAdjacentes(Adjacente(campoLargo))
    balsaNova.addCidadeAdjacentes(Adjacente(contenda))
    
    araucaria.addCidadeAdjacentes(Adjacente(curitiba))
    araucaria.addCidadeAdjacentes(Adjacente(contenda))
    
    saoJose.addCidadeAdjacentes(Adjacente(curitiba))
    saoJose.addCidadeAdjacentes(Adjacente(tijucas))
    
    contenda.addCidadeAdjacentes(Adjacente(balsaNova))
    contenda.addCidadeAdjacentes(Adjacente(araucaria))
    contenda.addCidadeAdjacentes(Adjacente(lapa))
    
    mafra.addCidadeAdjacentes(Adjacente(tijucas))
    mafra.addCidadeAdjacentes(Adjacente(lapa))
    mafra.addCidadeAdjacentes(Adjacente(canoinhas))
    
    tijucas.addCidadeAdjacentes(Adjacente(mafra))
    tijucas.addCidadeAdjacentes(Adjacente(saoJose))
    
    lapa.addCidadeAdjacentes(Adjacente(contenda))
    lapa.addCidadeAdjacentes(Adjacente(saoMateus))
    lapa.addCidadeAdjacentes(Adjacente(mafra))

    saoMateus.addCidadeAdjacentes(Adjacente(palmeira))
    saoMateus.addCidadeAdjacentes(Adjacente(irati))
    saoMateus.addCidadeAdjacentes(Adjacente(lapa)) 
    saoMateus.addCidadeAdjacentes(Adjacente(tresBarras))
    saoMateus.addCidadeAdjacentes(Adjacente(portoUniao))
    
    tresBarras.addCidadeAdjacentes(Adjacente(saoMateus))
    tresBarras.addCidadeAdjacentes(Adjacente(canoinhas))

