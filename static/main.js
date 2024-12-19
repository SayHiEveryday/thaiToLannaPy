document.getElementById("trans").addEventListener('click', translate);

async function translate() {
    const thaiText = document.getElementById('thai-text').value;

    const result = await fetch(`/api/trans/${thaiText}`, {
        method: "GET",
    });

    const val = await result.json();

    document.getElementById("lanna-text").value = val.result;
    
}