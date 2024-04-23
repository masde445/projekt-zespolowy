function updateThicknessOptions() {
    var materialSelect = document.getElementById('material');
    var thicknessSelect = document.getElementById('thickness');
    var material = materialSelect.value;

    // Usunięcie poprzednich opcji grubości
    thicknessSelect.innerHTML = '';

    // Ustawienie nowych opcji grubości w zależności od wybranego materiału
    if (material === 'stal ocynkowana') {
        addThicknessOptions(["0.5mm", "1mm", "3mm"]);
    } else if (material === 'stal nierdzewna') {
        addThicknessOptions(["1mm", "1.5mm", "2mm", "3mm", "4mm", "5mm", "6mm", "8mm"]);
    } else if (material === 'stal czarna') {
        addThicknessOptions(["1mm", "1.5mm", "2mm", "3mm", "4mm", "5mm", "6mm", "8mm", "10mm"]);
    }
}

function addThicknessOptions(thicknessOptions) {
    var thicknessSelect = document.getElementById('thickness');
    thicknessOptions.forEach(function (thickness) {
        var option = document.createElement('option');
        option.text = thickness;
        thicknessSelect.add(option);
    });
}

function analyzeDXF() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var material = document.getElementById('material').value;
    var thickness = document.getElementById('thickness').value;
    var requireMaterial = document.getElementById('requireMaterial').checked;

    // Prosta walidacja pliku
    if (!file) {
        alert("Proszę wybrać plik DXF.");
        return;
    }

    var formData = new FormData();
    formData.append('file', file);
    formData.append('material', material);
    formData.append('thickness', thickness);
    formData.append('requireMaterial', requireMaterial);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json()) // Odczytaj odpowiedź jako JSON
        .then(data => {
            // Wyświetl wyniki w divie results
            document.getElementById('results').innerHTML = `
                    <p>Calkowity obwód: ${data.total_perimeter}</p>
                    <p>Calkowite pole: ${data.total_area}</p>
                `;
        })
        .catch(error => {
            // Wyświetl błąd użytkownikowi
            document.getElementById('results').innerHTML = `<p>Błąd: ${error.message}</p>`;
            console.error('Error:', error);
        })
    }