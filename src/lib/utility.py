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