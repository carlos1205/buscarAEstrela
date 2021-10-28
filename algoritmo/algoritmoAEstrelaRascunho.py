from queue import PriorityQueue

a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
g = "G"
h = "H"
i = "I"
j = "J"
k = "K"
l = "L"
m = "M"
n = "N"
o = "O Vilcea"
p = "P"
q = "Q"
r = "R"
s = "S"
t = "T"
u = "U"

distrito_de_bucharest = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'RimnicuVilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

custo_da_distancia = {
    a: 0,
    b: 0,
    c: 0,
    d: 0,
    e: 0,
    f: 0,
    g: 0,
    g: 0,
    i: 0,
    j: 0,
    k: 0,
    l: 0,
    m: 0,
    n: 0,
    o: 0,
    p: 0,
    q: 0,
    r: 0,
    s: 0,
    t: 0,
    u: 0
}

mapa_da_romenia = {
    a: {
        c: 25,

    },
    c: {
        a: 25,
        b: 10,
        g: 20,

    },
    b: {
        d: 20,
        c: 10,

    },
    d: {
        b: 20,
        e: 15
    },
    e: {
        d: 15,
        f: 15
    },
    f: {
        e: 15,
        j: 20
    },
    g: {
        c: 20,
        h: 20,
        k: 10
    },
    h: {
        g: 20,
        i: 20,
        k: 20,
        l: 25
    },
    i: {
        h: 20,
        j: 20
    },
    j: {
        f: 20,
        m: 15
    },
    k: {
        g: 10,
        h: 20,
        n: 15
    },
    l: {
        h: 25,
        m: 20

    },
    m: {
        j: 15,
        l: 20,
        p: 25
    },
    n: {
        k: 15,
        o: 15,
        q: 20
    },
    o: {
        n: 15,
        o: 15,
        q: 20
    },
    p: {
        m: 25,
        o: 30,

    },
    q: {
        n: 25,
        o: 30
    },
    r: {
        q: 15,
        s: 10,

    },
    s: {
        r: 10,
        t: 15
    },
    t: {
        s: 15,
        u: 15
    },
    u: {
        t: 15
    }

}


def h(n):
    global distrito_de_bucharest
    return distrito_de_bucharest[n]


def g(n):
    global custo_da_distancia
    return custo_da_distancia[n]


def f(n):
    return h(n) + g(n)


def busca_A(raiz, objetivo):
    q = PriorityQueue()
    q.put((h(raiz), raiz, [raiz]))

    while not q.empty():
        frente = q.get()
        cidade = frente[1]
        if cidade is objetivo:
            print("Encontrado com {} de custo".format(frente[0]))
            print("Caminho:", frente[2])
            return

        cidades_adjacentes = mapa_da_romenia[cidade]
        for cidade_adjacente, custo in cidades_adjacentes.items():
            custo_da_distancia[cidade_adjacente] = custo_da_distancia[cidade] + custo
            q.put((f(cidade_adjacente), cidade_adjacente,
                  frente[2] + [cidade_adjacente]))


def main():
    busca_A(a, u)


main()
