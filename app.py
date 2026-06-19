import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from models.athlete import Athlete
from analyzer import TrainingAnalyzer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Training Analyzer Pro")

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

sarah = Athlete("Sarah", 240, 58.5)
backend_engine = TrainingAnalyzer(sarah)

def laod_data_event():
    backend_engine.load_data_from_csv("data/ride_data.csv")
    final_score = backend_engine.calculate_total_load()

    welcome_label.configure(
        text=f"Ride Data Loaded Successfully!\nTotal Weekly Stress: {final_score} TSS",
        text_color="#2ecc71"
        )
    
    chart_figure = backend_engine.plot_weekly_stress()

    canvas = FigureCanvasTkAgg(chart_figure, master=main_frame)
    canvas.draw()

    canvas.get_tk_widget().pack(pady=20)

sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="nsew")

logo_label = ctk.CTkLabel(sidebar_frame, text="Analyzer Pro", font=("Arial", 20, "bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20,10))

load_button = ctk.CTkButton(sidebar_frame, text="Load Ride Data", command=laod_data_event)
load_button.grid(row=1, column=0, padx=20, pady=10)

main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

welcome_label = ctk.CTkLabel(main_frame, text="Dashboard goes here...", font=("Arial", 28, "bold"))
welcome_label.pack(pady=200)

if __name__ == "__main__":
    print("Booting up the Graphical User Interface...")
    app.mainloop()