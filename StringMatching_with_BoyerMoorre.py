import tkinter as tk
from tkinter import filedialog

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

    skip = []
    for _ in range(10000):
        skip.append(m)
    for i in range(m - 1):
        skip[ord(pattern[i])] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(skip[ord(text[i])], m - j)
    
    return -1

def kalkulasiPersentasePlagiarisme(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    # kalau teks sama persis, otomatis 100%
    if text1 == text2:
        return 100.0

    # pisahkan text1 menjadi kalimat-kalimat
    sentences = text1.split('.')
    total_chars = len(text1)
    matched_chars = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        words = sentence.split()
        # cek substring 2 atau 3 kata
        for size in [3, 2]:
            for i in range(len(words) - size + 1):
                chunk = " ".join(words[i:i+size])
                if chunk in text2:
                    matched_chars += len(chunk)

    persentasePlagiarisme = (matched_chars / total_chars) * 100
    return min(persentasePlagiarisme, 100.0)



def analisisPlagiarisme(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read().replace('\n', '')
        text2 = f2.read().replace('\n', '')

    persentase_Plagiarisme = kalkulasiPersentasePlagiarisme(text1, text2)

    result_label.config(text="Tingkat Plagiarisme: " + str(persentase_Plagiarisme) + "%")
    text1_lines = text1.split('.')
    for line in text1_lines:
        if line.strip() in text2:
            analysis_text.insert(tk.END, line.strip() + '\n', 'bold')
        else:
            analysis_text.insert(tk.END, line.strip() + '\n')

def Mencari_file1():
    filename = filedialog.askopenfilename()
    file1_entry.delete(0, tk.END)
    file1_entry.insert(tk.END, filename)

def Mencari_file2():
    filename = filedialog.askopenfilename()
    file2_entry.delete(0, tk.END)
    file2_entry.insert(tk.END, filename)

def Menganalisa_files():
    file1 = file1_entry.get()
    file2 = file2_entry.get()

    if file1 and file2:
        analysis_text.delete(1.0, tk.END)
        analisisPlagiarisme(file1, file2)

# membuat sebuah tampilan mainWindow menggunakan Tkinter
window = tk.Tk()
window.title("pengecekan plagiarisasi")
window.geometry("500x400")

# membuat dan memposisikan widget
file1_label = tk.Label(window, text="File 1:")
file1_label.pack()

file1_entry = tk.Entry(window)
file1_entry.pack()

browse_file1_button = tk.Button(window, text="cariFile1", command=Mencari_file1)
browse_file1_button.pack()

file2_label = tk.Label(window, text="File 2:")
file2_label.pack()

file2_entry = tk.Entry(window)
file2_entry.pack()

browse_file2_button = tk.Button(window, text="cariFile2", command=Mencari_file2)
browse_file2_button.pack()

analyze_button = tk.Button(window, text="AnalisaPlagiarisasi", command=Menganalisa_files)
analyze_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

analysis_text = tk.Text(window, height=10, width=50)
analysis_text.pack()

# mengkonfigurasi analasisPlagiarisasi
analysis_text.tag_configure('bold', font=('Arial', 10, 'bold'))

# memulai GUI
window.mainloop()
