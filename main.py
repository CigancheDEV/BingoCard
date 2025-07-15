import tkinter as tk

def number_of_squares():
    input_text = input("Enter the number of squares to create: ")
    try:
        num_squares = int(input_text)
        if num_squares <= 0:
            print("Please enter a positive integer.")
            return

        # Create a Canvas widget to draw on
        size = calculateSizeOfCanvas(input("Enter game mode (1, 2, or 3): "))
        root = tk.Tk()
        root.title("Darko bingo")
        canvas = tk.Canvas(root, width=size[0], height=size[1], bg="white")
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

def calculateSizeOfCanvas(gameMode):
    if gameMode == '1':
        x = 500
        y = 500
    elif gameMode == '2':
        x = 800
        y = 800
    elif gameMode == '3':
        x = 1100
        y = 1100
    else:
        return ("Invalid game mode selected. Please choose 1, 2, or 3.")
    return [x,y] 

number_of_squares()