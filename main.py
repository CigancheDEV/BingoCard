import tkinter as tk

def number_of_squares():
    input_text = input("Enter the number of squares to create: ")
    try:
        num_squares = int(input_text)
        if num_squares <= 0:
            print("Please enter a positive integer.")
            return

        root = tk.Tk()
        root.title("Darko bingo")
        # Create a Canvas widget to draw on
        canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
        canvas.pack()
        # Draw squares with text
        for i in range(num_squares):
            x1 = 50 + (i % 10) * 100
            y1 = 50 + (i // 10) * 100
            x2 = x1 + 80
            y2 = y1 + 80
            canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"Test {i+1}", font=("Arial", 12))
        
        root.mainloop()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")



number_of_squares()