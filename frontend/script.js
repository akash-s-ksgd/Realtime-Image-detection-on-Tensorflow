document.addEventListener("DOMContentLoaded", function () {
    let video = document.getElementById("videoElement");
    let detectButton = document.getElementById("detectButton");

    if (!video) {
        console.error("❌ Error: No element with ID 'videoElement' found.");
        alert("⚠️ Camera setup failed: Video element not found in the HTML.");
        return;
    }

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            video.play();
            console.log("✅ Camera stream started!");
        })
        .catch(function (error) {
            console.error("❌ Camera error:", error.name, error.message);
            alert("⚠️ Camera access denied: " + error.message);
        });

    detectButton.addEventListener("click", function () {
        console.log("🔘 Detect button clicked!");

        if (!video.srcObject) {
            alert("⚠️ No video stream detected! Please check camera access.");
            return;
        }

        let canvas = document.createElement("canvas");
        let context = canvas.getContext("2d");

        if (video.videoWidth === 0 || video.videoHeight === 0) {
            alert("⚠️ Camera not ready. Please refresh the page and try again.");
            return;
        }

        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        canvas.toBlob(function (blob) {
            let formData = new FormData();
            formData.append("image", blob, "frame.jpg");

            console.log("📷 Image captured, sending to backend...");

            fetch("http://127.0.0.1:8000/detect", {
                method: "POST",
                body: formData,
                mode: "cors",
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Server responded with ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log("🔍 Detection Response:", data);
                alert("Detected objects: " + JSON.stringify(data.detected_objects));
                document.getElementById("results").innerHTML = `<h3>Detection Results</h3><pre>${JSON.stringify(data, null, 2)}</pre>`;
            })
            .catch(error => {
                console.error("❌ Fetch Error:", error);
                alert("❌ Error sending image for detection.");
            });
        }, "image/jpeg");
    });
});
