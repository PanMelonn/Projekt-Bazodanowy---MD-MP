$csvFolder = "C:\Users\grzag\Desktop\bazy\Projekt-Bazodanowy---MD-MP-main\CSV"

Get-ChildItem -Path $csvFolder -Filter *.csv | ForEach-Object {
    $fileName = $_.Name
    $tableName = $_.BaseName.ToLower()
    $remotePath = "/tmp/csv/$fileName"

    Write-Host "🔄 Importuję $fileName do tabeli $tableName"

    # Skopiuj plik do kontenera
    docker cp "$($_.FullName)" postgres-db:$remotePath

    # Wykonaj COPY wewnątrz kontenera
    $escapedCommand = "\copy $tableName FROM '$remotePath' WITH (FORMAT csv, HEADER true)"
    docker exec -it postgres-db psql -U user -d projectdb -c "$escapedCommand"
}
