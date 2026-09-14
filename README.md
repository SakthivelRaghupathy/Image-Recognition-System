# AI Vision: Intelligent Image Recognition Platform

AI Vision is a modern web application that bridges deep learning and intuitive user experience. It allows users to seamlessly upload real-world images and instantly receive accurate, AI-driven object classifications. 

## Theoretical Foundation & Concepts

At its core, this project demonstrates the practical application of **Convolutional Neural Networks (CNNs)** within a web-based ecosystem. 

* **The Architecture:** The system leverages **MobileNetV2**, a highly efficient CNN architecture designed specifically to minimize latency and computational load while maximizing accuracy. It uses depthwise separable convolutions, making it ideal for real-time web applications.
* **Image Preprocessing:** Before inference, raw user images are programmatically ingested via OpenCV, normalized, and dimensionally scaled to 224x224 pixels to match the exact tensor shape the neural network was trained on.
* **Inference & Softmax:** The processed tensor is passed through the model. The final layer uses a softmax activation function to output a probability distribution across 1,000 distinct ImageNet categories.
* **Confidence Thresholding:** The application applies programmatic logic to interpret the AI's output, rendering a definitive "Confirmed Match" only when the statistical confidence crosses a predefined threshold, ensuring reliable user feedback.

## Key Features

* **Real-Time Classification:** Delivers instant predictions using pre-trained ImageNet weights.
* **Top-K Prediction Mapping:** Extracts and visualizes the top 5 most statistically probable objects in an intuitive progress-bar format.
* **State-of-the-Art UI:** Features an asynchronous drag-and-drop upload zone, dynamic image preview generation, and responsive glass-morphism design elements.
* **Modular Application Factory:** Built on a highly scalable Flask architecture using Blueprints, ensuring enterprise-grade separation of concerns between routing, AI logic, and templating.

## Upcoming Features (Roadmap)

* **Custom Model Integration:** Transitioning from pre-trained ImageNet weights to custom-trained models for specialized object detection (e.g., specific retail products or medical imaging).
* **Database Persistence:** Integrating PostgreSQL to track user upload history, prediction analytics, and historical confidence trends.
* **REST API Expansion:** Developing dedicated backend endpoints to allow external clients and microservices to consume the image recognition pipeline.
* **Batch Processing:** Allowing users to upload multiple images simultaneously for asynchronous batch classification.

## Quick Start

```bash
# Clone the repository and setup the environment
git clone <repository-url>
cd image-Recognition-System
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies and launch
pip install -r requirements.txt
flask --app app run --debug
```
## Author
**SAKTHIVEL R**
