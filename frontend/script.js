document.addEventListener("DOMContentLoaded", function () {
    let video = document.getElementById("videoElement");
    let detectButton = document.getElementById("detectButton");

    // Request access to the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
        })
        .catch(function (error) {
            console.error("❌ Camera error:", error);
            alert("⚠️ Camera access denied. Please allow camera permissions in your browser settings.");
        });

    detectButton.addEventListener("click", function () {
        let canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");

        // Ensure video dimensions are available
        if (video.videoWidth === 0 || video.videoHeight === 0) {
            alert("⚠️ Camera not ready. Please refresh the page and try again.");
            return;
        }

        // Capture frame from video
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Convert to Blob and send to backend
        canvas.toBlob(function (blob) {
            let formData = new FormData();
            formData.append("image", blob, "frame.jpg");

            fetch("https://127.0.0.1:5000/detect", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log("Detection Response:", data);
                alert("Detected objects: " + JSON.stringify(data.detected_objects));
            })
            .catch(error => console.error("Error:", error));
        }, "image/jpeg");
    });
});
