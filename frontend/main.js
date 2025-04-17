async function sendMessage() {
  const input = document.getElementById('input').value;
  const res = await fetch('http://127.0.0.1:5000/api/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: input})
  });
  const data = await res.json();
  document.getElementById('output').innerText = data.response;
}