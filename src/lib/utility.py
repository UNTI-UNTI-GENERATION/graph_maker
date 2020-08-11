# csv関連関数群

def get_csv_template():
    """グラフ作成時のCSVのテンプレートを取得

    Returns:
        res: httpレスポンス
    """
    from io import StringIO
    from flask import make_response
    import csv
    f = StringIO()
    writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(['X軸名','凡例1名前','凡例2名前','凡例3名前','凡例4名前','凡例5名前'])
    writer.writerow(['','','','','',''])
    writer.writerow(['X軸データ','凡例1データ','凡例2データ','凡例3データ','凡例4データ','凡例5データ'])
    res = make_response()
    res.data = f.getvalue()
    res.headers['Content-Type'] = 'text/csv'
    res.headers['Content-Disposition'] = 'attachment; filename=demo.csv'
    return res

# check系関数群

def is_written_with_latex(input):
    """inputがLaTeX記法に則っているかどうか判定

    Args:
        input (String): 数式生成するためのLaTeXコード

    Returns:
        Bool: OK/True Wrong/False
    """
    # TODO: 厳密なチェック.いい方法が無い...
    if type(input) != 'str':
        return False
    return True