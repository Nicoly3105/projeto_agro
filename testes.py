
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
console = Console()

compras = []
encomendas = []
produtos = [{'Produto':'Vaca','Quantidade':56,'Unidade':'kg','Valor':56}]
animais = []
leite = []

def recibo_compras():
    print('\033[1;32m' + '~' * 100)
    print('~' * 40, 'RECIBO DE COMPRAS', '~' * 37)
    print('~' * 100, '\033[m')

    if len(compras) == 0:
        print('\033[1;31mNenhuma encomenda realizada!\033[m')
    else:
        table = Table(title="RECIBO DE COMPRAS")

        table.add_column("Item", justify="center")
        table.add_column("Tipo", justify="center")
        table.add_column("Descrição", justify="center")
        table.add_column("Quantidade", justify="center")
        table.add_column("Valor", justify="center")

        for i, compra in enumerate(compras, start=1):

            if 'Produto' in compra:
                table.add_row(
                    str(i),
                    "Produto",
                    compra['Produto'],
                    str(compra['Quantidade']),
                    f"R$ {compra['Valor']:.2f}"
                )

            if 'Animal' in compra:
                table.add_row(
                    str(i),
                    "Animal",
                    compra['Animal'],
                    str(compra['Quantidade']),
                    f"R$ {compra['Valor']:.2f}"
                )

        console.print(table)
    