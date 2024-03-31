import tkinter as tk

# Hàm để tạo ma trận Playfair từ khóa
def create_playfair_matrix(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    matrix = ''
    keyword = keyword.upper().replace('J', 'I')  

    for char in keyword:  
        if char not in matrix:
            matrix += char

    for char in alphabet: 
        if char not in matrix:
            matrix += char

    return matrix

# Hàm để mã hóa văn bản sử dụng ma trận Playfair
def playfair_cipher(plaintext, matrix):
    plaintext = plaintext.upper().replace('J', 'I')  
    ciphertext = ''

    # Chia văn bản thành các cặp ký tự
    pairs = []
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            pairs.append(plaintext[i] + 'X')  
        elif plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'X') 
        else:
            pairs.append(plaintext[i:i + 2])

    # Mã hoá từng cặp ký tự
    for pair in pairs:
        char1, char2 = pair
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5] + matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1] + matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]

    return ciphertext

# Hàm để xử lý sự kiện khi nhấn nút
def encrypt_text():
    keyword = keyword_entry.get()
    plaintext = plaintext_entry.get()

    matrix = create_playfair_matrix(keyword)
    ciphertext = playfair_cipher(plaintext, matrix)

    result_label.config(text=" RESULTS : " + ciphertext)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("truong phan")

# Tạo và định vị các widget với kích thước mở rộng
keyword_label = tk.Label(root, text="NHẬP KEY:")
keyword_label.grid(row=0, column=0, padx=10, pady=10)

keyword_entry = tk.Entry(root, width=40)
keyword_entry.grid(row=0, column=1, padx=10, pady=10)

plaintext_label = tk.Label(root, text="NHẬP TEXT:")
plaintext_label.grid(row=1, column=0, padx=10, pady=10)

plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = tk.Button(root, text="RUNNING", command=encrypt_text, width=30)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", width=60)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Chạy ứng dụng
root.mainloop()