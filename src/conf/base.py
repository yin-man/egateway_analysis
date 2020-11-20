# const
start_flag = "0x0B"
enter_flag = "0x0D"
end_flag = "0x1C"
msg_spliter = "<cr>"

USAGE = {
    "R": "必须",
    "RE": "必须",
    "O": "必须",
    "X": "可选",
}

# constance
meaning_of_each_column = {
    "SEQ": {"cn":"序号", "note":"表示该域在消息段里面的排列顺序"},
    "LEN": {"cn":"长度", "note":"表示该域的值的最大字符个数"},
    "DT": {"cn":"数据类型 ", "note":"表示该域的值的数据类型"},
    "Table#": {"cn":"表号", "note":"表示该域使用的表号(四位数字)"},
    "Usage": {"cn":"用法", "note":"表示该域的值是否必须", "vals": USAGE},
    "Cardinality": {"cn":"取值范围 ", "note":"表示该域的值的取值范围"},
    "ELEMENT": {"cn":"名称 ", "note":"表示该域的名称"},
}

#
