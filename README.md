## Sequence Alignment

### Overview

This web application provides a simple interface for aligning biological sequences using two popular algorithms: Needleman-Wunsch and Smith-Waterman. Users can upload their sequence files in FASTA format, select the desired algorithm, and obtain the alignment results along with the alignment score.

### Biological Background

#### What is Sequence Alignment?

Sequence alignment is a method used in bioinformatics to identify regions of similarity between DNA, RNA, or protein sequences. These regions of similarity can indicate functional, structural, or evolutionary relationships between the sequences.

#### Why is Sequence Alignment Important?

- **Functional Annotation**: Understanding the function of a gene or protein by comparing it to sequences with known functions.
- **Phylogenetic Analysis**: Studying the evolutionary relationships between organisms.
- **Structural Prediction**: Inferring the three-dimensional structure of a sequence based on known structures.
- **Variant Detection**: Identifying mutations or variations in sequences that may be linked to diseases.

### Algorithms

#### Needleman-Wunsch Algorithm

The Needleman-Wunsch algorithm is a global alignment algorithm used to align sequences end-to-end. It is suitable for sequences of similar length and is used to find the best possible alignment over the entire length of the sequences.

##### How it Works:
1. **Initialization**: Create a matrix and initialize the first row and column with gap penalties.
2. **Matrix Filling**: Fill in the matrix based on match, mismatch, and gap scores.
3. **Traceback**: Starting from the bottom-right of the matrix, trace back to find the optimal alignment.

#### Smith-Waterman Algorithm

The Smith-Waterman algorithm is a local alignment algorithm used to find the best alignment within subsequences of the sequences. It is suitable for aligning sequences that may have regions of high similarity within otherwise unrelated sequences.

##### How it Works:
1. **Initialization**: Create a matrix and initialize the first row and column with zeros.
2. **Matrix Filling**: Fill in the matrix based on match, mismatch, and gap scores, ensuring no negative values.
3. **Traceback**: Starting from the highest value in the matrix, trace back to find the optimal local alignment.

### Application Features

- **Upload Sequences**: Users can upload two FASTA files containing the sequences to be aligned.
- **Select Algorithm**: Users can choose between Needleman-Wunsch and Smith-Waterman algorithms.
- **Display Results**: The application displays the aligned sequences, a match string, and the alignment score.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/itsknk/sequence_alignment.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sequence_alignment
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Upload two FASTA files containing the sequences you want to align.
3. Select the desired alignment algorithm (Needleman-Wunsch or Smith-Waterman).
4. Click the "Align" button.
5. View the alignment results and score on the results page.

## File Descriptions

- `app.py`: The main Flask application file.
- `templates/index.html`: The main page template for uploading files and selecting the algorithm.
- `templates/result.html`: The result page template for displaying the alignment results.
- `static/style.css`: The CSS file for styling the web pages.
- `algorithms/needleman_wunsch.py`: Implementation of the Needleman-Wunsch algorithm.
- `algorithms/smith_waterman.py`: Implementation of the Smith-Waterman algorithm.
