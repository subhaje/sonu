# Car Panel Dent Detection System

This project implements a machine learning system for detecting dents in car panels using computer vision techniques. The system can analyze images of car panels and identify whether they contain dents.

## Project Structure

```
.
├── app.py                 # Web interface for dent detection
├── data/                  # Dataset directory
│   ├── dent/             # Images of dented panels
│   └── no_dent/          # Images of non-dented panels
├── source_images/         # Raw source images
├── dent_detection.py      # Core detection logic
├── train.py              # Model training script
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd dent-detection
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset Preparation

### Image Requirements
- Format: JPG, JPEG, or PNG
- Resolution: Minimum 224x224 pixels
- Lighting: Well-lit images with minimal glare
- Focus: Clear, sharp images
- Background: Consistent, neutral background when possible

### Steps to Prepare Dataset

1. Download sample images:
   ```bash
   python source_images/download_samples.py
   ```

2. Organize images into training data:
   ```bash
   python data/prepare_dataset.py
   ```
   This will sort images into dent/no_dent categories.

## Training the Model

1. Start the training process:
   ```bash
   python train.py
   ```

2. Monitor the training progress in the console output.

## Using the Web Interface

1. Start the web server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Upload an image through the web interface to detect dents.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.