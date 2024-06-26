{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebe94fbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog, messagebox\n",
    "from tkinter import ttk\n",
    "import spacy\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "# Load spaCy model\n",
    "nlp = spacy.load('en_core_web_sm')\n",
    "\n",
    "def preprocess_text(text):\n",
    "    doc = nlp(text.lower())\n",
    "    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]\n",
    "    return ' '.join(tokens)\n",
    "\n",
    "def vectorize_texts(texts):\n",
    "    vectorizer = TfidfVectorizer()\n",
    "    tfidf_matrix = vectorizer.fit_transform(texts)\n",
    "    return tfidf_matrix, vectorizer\n",
    "\n",
    "def calculate_similarity(tfidf_matrix):\n",
    "    similarity_matrix = cosine_similarity(tfidf_matrix)\n",
    "    return similarity_matrix\n",
    "\n",
    "def plagiarism_detection(documents):\n",
    "    preprocessed_texts = [preprocess_text(text) for text in documents]\n",
    "    preprocessed_texts = [text for text in preprocessed_texts if text.strip()]\n",
    "    if not preprocessed_texts:\n",
    "        raise ValueError(\"All documents are empty after preprocessing.\")\n",
    "    tfidf_matrix, vectorizer = vectorize_texts(preprocessed_texts)\n",
    "    similarity_matrix = calculate_similarity(tfidf_matrix)\n",
    "    return similarity_matrix\n",
    "\n",
    "class PlagiarismDetectionApp:\n",
    "    def __init__(self, root):\n",
    "        self.root = root\n",
    "        self.root.title(\"Plagiarism Detection Tool\")\n",
    "        self.root.geometry(\"900x700\")\n",
    "        self.root.configure(bg='#f0f8ff')  # Light blue background\n",
    "\n",
    "        self.documents = []\n",
    "\n",
    "        style = ttk.Style()\n",
    "        style.configure('TButton', font=('Times New Roman', 12), padding=10, foreground='black', background='#ffffff')\n",
    "        style.configure('TLabel', font=('Times New Roman', 12), background='#f0f8ff')\n",
    "\n",
    "        # Title Label\n",
    "        title_label = ttk.Label(self.root, text=\"Plagiarism Detection Tool\", font=('Times New Roman', 18, 'bold'), background='#4682b4', foreground='white')\n",
    "        title_label.pack(pady=10, padx=10, fill='x')\n",
    "        title_label.config(anchor='center')\n",
    "\n",
    "        # Frame for text area and buttons\n",
    "        frame = tk.Frame(self.root, bg='#f0f8ff')\n",
    "        frame.pack(pady=10)\n",
    "\n",
    "        self.text_area = tk.Text(frame, height=10, width=80, wrap='word', bg='#ffffff', fg='#000000', font=('Times New Roman', 12))\n",
    "        self.text_area.pack(side=tk.LEFT, padx=(0, 10))\n",
    "        \n",
    "        # Add scrollbar to text area\n",
    "        scrollbar = tk.Scrollbar(frame, command=self.text_area.yview)\n",
    "        scrollbar.pack(side=tk.LEFT, fill=tk.Y)\n",
    "        self.text_area.config(yscrollcommand=scrollbar.set)\n",
    "\n",
    "        button_frame = tk.Frame(self.root, bg='#f0f8ff')\n",
    "        button_frame.pack(pady=10)\n",
    "\n",
    "        self.load_button = tk.Button(button_frame, text=\"Load Text Files\", command=self.load_files, font=('Times New Roman', 12, 'bold'), bg='#ffffff')\n",
    "        self.load_button.grid(row=0, column=0, padx=10, pady=5)\n",
    "\n",
    "        self.add_button = tk.Button(button_frame, text=\"Add Text\", command=self.add_text, font=('Times New Roman', 12, 'bold'), bg='#ffffff')\n",
    "        self.add_button.grid(row=0, column=1, padx=10, pady=5)\n",
    "\n",
    "        self.detect_button = tk.Button(button_frame, text=\"Detect Plagiarism\", command=self.detect_plagiarism, font=('Times New Roman', 12, 'bold'), bg='#ffffff')\n",
    "        self.detect_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)\n",
    "\n",
    "        self.result_text = tk.Text(self.root, height=15, width=100, wrap='word', bg='#ffffff', fg='#000000', font=('Times New Roman', 12), state='disabled')\n",
    "        self.result_text.pack(pady=20)\n",
    "\n",
    "        # Add scrollbar to result text area\n",
    "        result_scrollbar = tk.Scrollbar(self.result_text, command=self.result_text.yview)\n",
    "        self.result_text.config(yscrollcommand=result_scrollbar.set)\n",
    "        result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)\n",
    "\n",
    "        # Similarity Value Section\n",
    "        similarity_value_frame = tk.Frame(self.root, bg='#f0f8ff')\n",
    "        similarity_value_frame.pack(pady=(10, 5))\n",
    "\n",
    "        similarity_value_label = ttk.Label(similarity_value_frame, text=\"Similarity Value:\", font=('Times New Roman', 14), background='#f0f8ff')\n",
    "        similarity_value_label.pack(side=tk.LEFT, padx=(0, 10))\n",
    "\n",
    "        self.similarity_value_entry = tk.Entry(similarity_value_frame, font=('Times New Roman', 14), state='readonly', justify='center', width=10)\n",
    "        self.similarity_value_entry.pack(side=tk.LEFT)\n",
    "\n",
    "        # Verbal Feedback Label\n",
    "        self.feedback_label = ttk.Label(self.root, text=\"\", font=('Times New Roman', 14, 'bold'), background='#f0f8ff')\n",
    "        self.feedback_label.pack(pady=10)\n",
    "\n",
    "    def load_files(self):\n",
    "        file_paths = filedialog.askopenfilenames(filetypes=[(\"Text files\", \"*.txt\")])\n",
    "        if file_paths:\n",
    "            for file_path in file_paths:\n",
    "                try:\n",
    "                    with open(file_path, 'r', encoding='utf-8') as file:\n",
    "                        text = file.read()\n",
    "                except UnicodeDecodeError:\n",
    "                    with open(file_path, 'r', encoding='latin-1') as file:\n",
    "                        text = file.read()\n",
    "                self.documents.append(text)\n",
    "                self.text_area.insert(tk.END, f\"Loaded file: {file_path}\\n{text}\\n{'-'*40}\\n\")\n",
    "            messagebox.showinfo(\"Success\", f\"Loaded {len(file_paths)} files successfully.\")\n",
    "\n",
    "    def add_text(self):\n",
    "        text = self.text_area.get(1.0, tk.END).strip()\n",
    "        if text:\n",
    "            self.documents.append(text)\n",
    "            self.text_area.delete(1.0, tk.END)\n",
    "            messagebox.showinfo(\"Success\", \"Text added successfully.\")\n",
    "        else:\n",
    "            messagebox.showwarning(\"Warning\", \"No text to add.\")\n",
    "\n",
    "    def detect_plagiarism(self):\n",
    "        if len(self.documents) < 2:\n",
    "            messagebox.showwarning(\"Warning\", \"Please add at least two documents.\")\n",
    "            return\n",
    "\n",
    "        try:\n",
    "            similarity_matrix = plagiarism_detection(self.documents)\n",
    "            result_text = \"Similarity Matrix:\\n\"\n",
    "            plagiarism_detected = False\n",
    "\n",
    "            for i, row in enumerate(similarity_matrix):\n",
    "                for j, similarity in enumerate(row):\n",
    "                    if i != j:\n",
    "                        if similarity > 0.5:\n",
    "                            result_text += f\"Document {i + 1} and Document {j + 1}: {similarity * 100:.2f}% similar (Potential Plagiarism Detected)\\n\"\n",
    "                            plagiarism_detected = True\n",
    "                        else:\n",
    "                            result_text += f\"Document {i + 1} and Document {j + 1}: {similarity * 100:.2f}% similar\\n\"\n",
    "\n",
    "            if plagiarism_detected:\n",
    "                result_text += \"\\nPlagiarism Detected.\"\n",
    "                feedback_text = \"Plagiarism Detected!\"\n",
    "                feedback_value = \"0\"  # Changed from 1 to 0 as per request\n",
    "                feedback_color = '#ff0000'  # Red\n",
    "            else:\n",
    "                result_text += \"\\nNo Plagiarism Detected.\"\n",
    "                feedback_text = \"No Plagiarism Detected.\"\n",
    "                feedback_value = \"1\"  # Changed from 0 to 1 as per request\n",
    "                feedback_color = '#008000'  # Green\n",
    "\n",
    "            self.result_text.config(state='normal')\n",
    "            self.result_text.delete(1.0, tk.END)\n",
    "            self.result_text.insert(tk.END, result_text)\n",
    "            self.result_text.config(state='disabled')\n",
    "\n",
    "            self.feedback_label.config(text=feedback_text, foreground=feedback_color)\n",
    "\n",
    "            self.similarity_value_entry.config(state='normal')\n",
    "            self.similarity_value_entry.delete(0, tk.END)\n",
    "            self.similarity_value_entry.insert(0, feedback_value)\n",
    "            self.similarity_value_entry.config(state='readonly')\n",
    "\n",
    "        except ValueError as e:\n",
    "            messagebox.showwarning(\"Warning\", str(e))\n",
    "        \n",
    "        self.documents = []\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    root = tk.Tk()\n",
    "    app = PlagiarismDetectionApp(root)\n",
    "    root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3825058f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bff9a075",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
