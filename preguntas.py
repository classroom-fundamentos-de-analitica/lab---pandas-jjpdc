"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    p1 = len(df0.axes[0]) 
    return p1

   


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    import pandas as pd

    df0 = pd.read_csv("tbl0.tsv", sep='\t')
    p1 = df0.shape
     return(p1[1])
   


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    import pandas as pd
    df = pd.read_csv("data.tsv", sep = '\t')
    p1 = df.groupby('_c1').count()['_c0']
 
    return p1


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    
    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    p2 = df0.groupby('_c1').mean()['_c2']
    return p2


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    p5 = df0.groupby('_c1').max()['_c2']
    return(p5)
    


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import pandas as pd
    df1 = pd.read_csv("tbl1.tsv", sep = '\t')
    p4 = list(set(df1['_c4']))
    p4.sort()
    mayusculas = []
    for i in p4:
      mayusculas.append(i.upper())
    return mayusculas
    


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    p5 = df0.groupby('_c1').sum()['_c2']
    return p5


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    df0['suma'] = df0['_c0'] + df0['_c2']
    return df0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    anos = []
    for i in df0['_c3']:
        anos.append(i.split('-')[0])
    df0['anos'] = anos

    return df0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    
    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    p8 = list(set(df0['_c1']))
    p8.sort()
    p8
    lista = []
    for i in p8:
      num = []
      union = ""
      for o in df0.index:
        if(i == df0['_c1'][o]):
          num.append(df0['_c2'][o])
      num.sort()
      for o in num:
        union += str(o)
        if(num.index(o)<len(num)-1):
          union += ":"
      lista.append(union)
    resultado = pd.DataFrame({'_c0':p8, 'lista':lista})
    
    return resultado
    


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    import pandas as pd
    df1 = pd.read_csv("tbl1.tsv", sep = '\t')
    num = list(set(df1['_c0']))
    num.sort()
    lista = []
    for i in num:
      letras = []
      union = ""
      for o in df1.index:
        if (df1['_c0'][o] == i):
          letras.append(df1['_c4'][o])
      letras.sort()
      for o in letras:
        union += str(o)
        if(letras.index(o)<len(letras)-1):
          union += ","
      lista.append(union)
    resultado = pd.DataFrame({'_c0':num, 'lista':lista})
    
    return resultado
    


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    import pandas as pd
    df2 = pd.read_csv("tbl2.tsv", sep = '\t')
    num = list(set(df2['_c0']))
    num.sort()
    lista = []
    lista2 = []
    listadf = []
    for i in num:
      letras = []
      derecha = []
      union = ""
      for o in df2.index:
        if (i == df2['_c0'][o]):
          letras.append(df2['_c5a'][o])
          derecha.append(df2['_c5b'][o])
      for o in letras:
        union += str(o)
        union += ":"
        union += str(derecha[letras.index(o)])
        if (letras.index(o)<len(letras)-1):
          union += ","
      lista.append(union)
    for i in lista:
      l = []
      for o in i.split(','):
        l.append(o)
      lista2.append(l)
    for i in lista2:
      i.sort()
      union = ""
      for o in i:
        union += str(o)
        if (i.index(o) < len(i)-1):
          union += ","
      listadf.append(union)
    resultado = pd.DataFrame({'_c0':num, 'lista':listadf})
 
    return resultado
   


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    import pandas as pd
    df0 = pd.read_csv("tbl0.tsv", sep = '\t')
    df2 = pd.read_csv("tbl2.tsv", sep = '\t')
    p11 = pd.merge(df0, df2, on = "_c0")
    resultado = p11.groupby('_c1').sum()['_c5b']
    return resultado
   
