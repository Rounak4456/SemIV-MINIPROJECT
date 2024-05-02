import tkinter as tk
from tkinter import messagebox

class MatrixOperations:

    def multiply_matrices(mat_a, mat_b):
        rows_a  = len(mat_a)
        cols_a = len(mat_a[0])
        rows_b = len(mat_b) 
        cols_b = len(mat_b[0])
        if cols_a != rows_b:
            return None

        result_mat = [[0.0] * cols_b for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                result_mat[i][j] = sum(mat_a[i][k] * mat_b[k][j] for k in range(cols_a))

        return result_mat
    
    def multiply_matrix_vector(matrix, vector):
        result = [0.0] * len(matrix)    
        for i in range(len(matrix)):
            for j in range(len(vector)):
                result[i] += matrix[i][j] * vector[j]
        print(result)
        return result

    def display_matrix(matrix, iter, TxtArea):
        TxtArea.insert('1.0', "The Distribution after "+str(iter)+ " iterations is : \n")
        for row in matrix:
            for element in row:
                TxtArea.insert(tk.END, str(element) + ' ')
            TxtArea.insert(tk.END, '\n')

    def power_matrix(matrix, n):
        result_n = matrix.copy()
        for i in range(1, n):
            result_n = MatrixOperations.multiply_matrices(result_n, matrix)
        return result_n
    
    def is_column_sum(matrix):
        num_rows = len(matrix)
        num_cols =  len(matrix[0])
        for j in range(num_cols):
            column_sum = sum(matrix[i][j] for i in range(num_rows))
            if abs(column_sum - 1.0) > 1e-6:
                return False

        return True

def MarkovAnalysis(matrix1, matrix2, iter, TextArea):
    iteration = int(iter.get())
    result_n = []
    final_result = []
    if MatrixOperations.is_column_sum(matrix1):
        result_n = MatrixOperations.power_matrix(matrix1, iteration)
        final_result = MatrixOperations.multiply_matrix_vector(result_n, matrix2)
    else:
        messagebox.showwarning("Stochasticity", "The sum of probabilities in each column should be equal to 1.")
    TextArea.delete("1.0", "end")
    TextArea.insert('1.0', "The Distribution after "+str(iteration)+" iterations is : \n")
    for element in final_result:
        TextArea.insert(tk.END, str(round(element)) + ' ')
        TextArea.insert(tk.END, '\n')

def calc(matrix1, matrix2):
    #print("Dist mat", matrix2)
    final_window = tk.Toplevel(root)
    final_window.title("RESULT")
    final_window.geometry("500x500")
    final_window.configure(bg="lightblue")  # Set background color

    lbl = tk.Label(final_window, text="Enter the number of iterations:", font=("Arial", 16), bg="lightblue")  # Set background color
    lbl.pack()

    iter = tk.Entry(final_window, width=10, font=("Arial", 16), justify="center")
    iter.pack(pady=10)

    Txt = tk.Text(final_window, font=("Arial", 16))
    Txt.place(x=0, y=110, width=500, height=300)

    calculate = tk.Button(final_window, text="CALCULATE", command=lambda: MarkovAnalysis(matrix1, matrix2, iter, Txt), bg="green", fg="white")  # Set background and foreground colors
    calculate.pack()

def dist_matrix(order, matrix1):
    another_window = tk.Toplevel(root)
    another_window.title("Distribution Matrix")
    another_window.configure(bg="lightgreen")  # Set background color

    mat2 = [tk.Entry(another_window, width=5, font=("Arial", 14), justify='center') for _ in range(order)]
    for i in range(order):
        mat2[i].grid(row=i, column=0, padx=5, pady=5)
    
    def proceed_to_calc():
        dist_mat = [float(entry.get()) if entry.get() else 0 for entry in mat2]
        calc(matrix1, dist_mat)

    button2 = tk.Button(another_window, text="NEXT", command=proceed_to_calc, bg="blue", fg="white")  # Set background and foreground colors
    button2.grid(row=order, columnspan = order, pady = 10)

def prob_matrix(order):
    matrix_window = tk.Toplevel(root)
    matrix_window.title("Probability Matrix")
    matrix_window.configure(bg="lightyellow")  # Set background color

    mat1 = [[tk.Entry(matrix_window, width=5, font=("Arial", 14), justify='center') for _ in range(order)] for _ in range(order)]
    for i in range(order):
        for j in range(order):
            mat1[i][j].grid(row=i, column=j, padx=5, pady=5)

    def proceed_to_dist_matrix():
        prob_mat = [[float(entry.get()) if entry.get() else 0 for entry in row] for row in mat1]
        dist_matrix(order, prob_mat)

    button1 = tk.Button(matrix_window, text="NEXT", command=proceed_to_dist_matrix, bg="orange", fg="white")  # Set background and foreground colors
    button1.grid(row=order, columnspan=order, pady=10)

# Main window
root = tk.Tk()
root.title("MARKOV CALCULATOR")
root.geometry("300x150")
root.configure(bg="lightgrey")  # Set background color

label = tk.Label(root, text="Enter the order of the matrix:", font=("Arial", 16), bg="lightgrey")  # Set background color
label.pack(pady=10)

entry = tk.Entry(root, width=10, font=("Arial", 16), justify="center")
entry.pack(pady=10)

submit_button = tk.Button(root, text="Create Matrix", font=("Arial", 12), command=lambda: prob_matrix(int(entry.get())), bg="purple", fg="white")  # Set background and foreground colors
submit_button.pack(pady=10)

root.mainloop()