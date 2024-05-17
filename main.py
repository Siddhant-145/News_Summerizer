import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')


def summerize(): 
    input_type = input_var.get()  # Get the selected input type (URL or Text)
    input_data = utext.get('1.0',"end").strip()  # Get the input data (URL or Text)

    if input_type == "URL":
        article = Article(input_data)
        article.download()
        article.parse()
        article.nlp()
        text = article.text
    else:
        text = input_data

    analysis = TextBlob(text)

    title.config(state='normal')
    sum.config(state='normal')
    polar.config(state ='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0','end')
    title.insert('1.0', article.title if input_type == "URL" else "User Input Article")
    sum.delete('1.0','end')
    sum.insert('1.0', article.summary if input_type == "URL" else text)
    polar.delete('1.0',"end")
    polar.insert('1.0', analysis.polarity)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f"Sentiment: {'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral'}")
    
    title.config(state='disabled')
    sum.config(state='disabled')
    polar.config(state='disabled')
    sentiment.config(state='disabled')


root = tk.Tk()
root.title("News summarizer")
root.geometry('1400x700')

# Radio button to choose input type (URL or Text)
input_var = tk.StringVar()
input_var.set("URL")
url_radio = tk.Radiobutton(root, text="URL", variable=input_var, value="URL")
url_radio.pack()
text_radio = tk.Radiobutton(root, text="Text", variable=input_var, value="Text")
text_radio.pack()

tlabel = tk.Label(root,text = "Title")
tlabel.pack()
title = tk.Text(root, height = 1, width = 150 )
title.config(state = 'disabled', bg ='#dddddd')
title.pack()

slabel = tk.Label(root,text = "Summary")
slabel.pack()
sum = tk.Text(root, height = 25, width = 150 )
sum.config(state = 'disabled', bg ='#dddddd')
sum.pack()

p_label = tk.Label(root,text = "Polarity")
p_label.pack()
polar = tk.Text(root, height = 1, width = 150 )
polar.config(state = 'disabled', bg ='#dddddd')
polar.pack()

sa_label = tk.Label(root,text = "Sentiment Analysis")
sa_label.pack()
sentiment = tk.Text(root, height = 1, width = 150 )
sentiment.config(state = 'disabled', bg ='#dddddd')
sentiment.pack()

ulabel = tk.Label(root,text = "Url/Text")
ulabel.pack()
utext = tk.Text(root, height = 1, width = 150 )
utext.pack()

btn = tk.Button(root, text ="Summarize" , command= summerize)
btn.pack()

root.mainloop()
