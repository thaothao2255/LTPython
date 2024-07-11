# Đọc dữ liệu từ tệp fin.txt và tính tổng các số
def read_and_compute_sum(input_file):
    with open(input_file, 'r') as fin:
        lines = fin.readlines()
        n = int(lines[0])  # Số tự nhiên n

        # Tính tổng tất cả các số
        total_sum = sum([sum(map(float, line.split())) for line in lines[1:]])

        # Ghi dữ liệu vào tệp fout.txt
        with open('fout.txt', 'w') as fout:
            fout.write(f"{total_sum}\n")  # Ghi tổng tất cả các số vào dòng đầu tiên

            # Tính và ghi tổng của từng dãy số vào các dòng tiếp theo
            for line in lines[1:]:
                numbers = list(map(float, line.split()))
                line_sum = sum(numbers)
                fout.write(f"{line_sum}\n")  # Ghi tổng của dãy số vào tệp fout.txt

# Đọc dữ liệu từ tệp fin.txt và ghi kết quả vào fout.txt
read_and_compute_sum('fin.txt')
