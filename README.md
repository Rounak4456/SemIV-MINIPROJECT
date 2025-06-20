# Markov Chain Text Generator

A Python-based graphical application that generates text using Markov chain algorithms. This tool allows users to input text corpus either by typing directly or uploading files, and generates coherent text sequences based on the statistical patterns learned from the input.

## ✨ Features

### Core Functionality
- **Dual Input Methods**: Type text directly or upload text files
- **Markov Chain Text Generation**: Uses first-order Markov chains for text generation
- **Customizable Parameters**: 
  - Adjustable word limit (20-100 words)
  - Custom seed word selection
  - Multiple text variations generation
- **User-Friendly GUI**: Modern interface built with CustomTkinter
- **Theme Support**: Light and dark mode toggle
- **Batch Generation**: Generates 10 different text variations simultaneously

### Interface Features
- **Tabbed Interface**: Separate tabs for different input methods
- **Real-time Controls**: Interactive slider for word limit adjustment
- **File Browser**: Easy file selection with dialog box
- **Responsive Design**: Organized layout with proper spacing and alignment

## 📸 Screenshots

### Main Interface - Type Text Tab
*[Add screenshot of the main interface showing the "Type Text" tab with input corpus area, generated text area, and controls]*

### File Upload Tab
*[Add screenshot of the "Choose a file" tab showing file upload functionality and text generation]*

### Dark Mode Interface
*[Add screenshot showing the application in dark mode]*

### Text Generation Example
*[Add screenshot showing example input text and the corresponding generated output]*

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Required Dependencies
```bash
pip install customtkinter
```

Note: `tkinter` comes pre-installed with Python, so no additional installation is required for it.

### Setup
1. Clone or download the project files
2. Ensure all dependencies are installed
3. Run the application:
```bash
python markov_text_generator.py
```

## 📖 Usage

### Method 1: Type Text Directly

1. **Launch the Application**: Run the Python script
2. **Select "Type Text" Tab**: This tab is selected by default
3. **Input Corpus Text**: 
   - Click in the left text area
   - Replace "Enter Corpus Text" with your training text
   - The more text you provide, the better the generation quality
4. **Set Parameters**:
   - Use the slider to adjust word limit (20-100 words)
   - Enter a seed word in the "Enter Seed Word" field
5. **Generate Text**: Click "Generate Text" button
6. **View Results**: Generated text variations appear in the right panel

### Method 2: Upload Text File

1. **Switch to "Choose a file" Tab**
2. **Upload File**: Click "Open File" button and select a text file
3. **Set Parameters**:
   - Enter seed word in the designated field
   - Specify maximum word limit
4. **Generate Text**: Click "Generate Text" button
5. **Review Output**: Multiple text variations will be displayed

### Additional Features

- **Theme Toggle**: Use the "Dark Mode" switch in the top-right corner
- **Real-time Preview**: Word limit changes are reflected immediately
- **Multiple Outputs**: Each generation produces 10 different text variations

## 🔧 How It Works

### Markov Chain Fundamentals

A Markov chain is a mathematical model that predicts the next state based solely on the current state, without considering the sequence of events that led to it. In text generation:

1. **Current State**: The current word in the sequence
2. **Next State**: The word that follows, chosen based on probability
3. **Memory**: Only the immediate previous word influences the next choice

### Text Generation Process

#### 1. Text Preprocessing
The preprocessing step:
- Normalizes text to lowercase for consistency
- Removes punctuation to focus on word relationships
- Splits text into individual words for analysis

#### 2. Markov Model Construction
The model building process:
- Creates a dictionary where each word maps to a list of possible next words
- Scans through the entire text, recording word pairs
- Builds statistical relationships between consecutive words

**Example**: For text "the cat sat on the mat", the model would be:
```
{
    'the': ['cat', 'mat'],
    'cat': ['sat'],
    'sat': ['on'],
    'on': ['the'],
    'mat': []
}
```

#### 3. Probabilistic Text Generation
The generation algorithm:
1. **Starts with Seed Word**: Uses user-provided seed as the first word
2. **Calculates Probabilities**: For each possible next word, calculates its probability based on frequency in training data
3. **Weighted Random Selection**: Chooses next word using weighted random selection (more frequent words have higher probability)
4. **Iterative Process**: Repeats until reaching maximum length or hitting a dead end
5. **Output Formation**: Joins all selected words into coherent text

### Statistical Foundation

The probability of selecting word B after word A is:
```
P(B|A) = Count(A→B) / Count(A→any_word)
```

Where:
- `Count(A→B)` is how many times word B follows word A in the training text
- `Count(A→any_word)` is the total number of words that follow word A

## 🏗️ Technical Implementation

### Architecture Overview

The application follows a modular design with clear separation of concerns:

#### Core Components

1. **Text Processing Module**
   - `preprocess_text()`: Text normalization and cleaning
   - `build_markov_model()`: Statistical model construction

2. **Generation Engine**
   - `generate_text_from_model()`: Core generation algorithm
   - `generate_text1()`: Alternative generation function for file input

3. **User Interface Layer**
   - CustomTkinter-based GUI
   - Tabbed interface design
   - Real-time control updates

4. **File Management**
   - `open_file()`: File dialog and reading functionality
   - Text area population and management

### Performance Considerations

- **Memory Usage**: Model size grows with corpus vocabulary
- **Generation Speed**: O(n) where n is the desired output length
- **Preprocessing Time**: O(m) where m is the input corpus size

## 📦 Dependencies

### Primary Dependencies
- **customtkinter**: Modern GUI framework for enhanced visual appeal
- **tkinter**: Standard Python GUI library (included with Python)
- **random**: Random number generation for probabilistic selection
- **string**: String manipulation utilities

### Python Standard Library Modules Used
- `filedialog`: File selection dialogs
- `random`: Weighted random selection
- `string`: Text processing utilities

## 🤝 Contributing

We welcome contributions to improve the Markov Chain Text Generator! Here's how you can help:

### Ways to Contribute
1. **Bug Reports**: Report issues or unexpected behavior
2. **Feature Requests**: Suggest new functionality
3. **Code Improvements**: Optimize algorithms or add features
4. **Documentation**: Improve README or add code comments
5. **Testing**: Test with different text types and report results

### Development Guidelines
- Follow Python PEP 8 style guidelines
- Add comments for complex algorithms
- Test with various text inputs
- Ensure GUI responsiveness

### Potential Enhancements
- **Higher-order Markov chains**: Consider 2-3 previous words
- **Export functionality**: Save generated text to files
- **Text analysis**: Display statistics about the corpus
- **Advanced preprocessing**: Handle different languages or formats
- **Batch processing**: Process multiple files simultaneously
