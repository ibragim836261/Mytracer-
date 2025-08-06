async function startCamera() {
  const email = document.getElementById('email').value;
  if (!email) return alert("Введи почту");

  const stream = await navigator.mediaDevices.getUserMedia({ video: true });
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  video.srcObject = stream;
  video.play();

  setTimeout(async () => {
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const photo = canvas.toDataURL('image/jpeg');

    const res = await fetch("https://api64.ipify.org?format=json");
    const { ip } = await res.json();

    await fetch("http://localhost:5000/send_data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, ip, photo })
    });

    alert("Данные отправлены");
    stream.getTracks().forEach(t => t.stop());
  }, 3000);
}
