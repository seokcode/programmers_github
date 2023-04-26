def flip_bits(binary_str):
    """
    2진수 문자열(binary_str)에서 0을 1로, 1을 0으로 뒤집는 함수

    Args:
        binary_str (str): 2진수 문자열

    Returns:
        str: 변환된 2진수 문자열
    """
    flipped_str = ""
    for char in binary_str:
        if char == '0':
            flipped_str += '1'  # 0을 1로 뒤집어서 추가
        elif char == '1':
            flipped_str += '0'  # 1을 0으로 뒤집어서 추가
        else:
            raise ValueError("2진수 문자열(binary_str)은 0과 1로만 이루어져야 합니다.")
    return flipped_str


# Unit Test
assert flip_bits("10101") == "01010"
assert flip_bits("110010") == "001101"
assert flip_bits("0") == "1"
assert flip_bits("1") == "0"
assert flip_bits("") == ""
