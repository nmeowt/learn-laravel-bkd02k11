<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <h1>Danh sách lớp</h1>
    <a href="{{ route('grade.create') }}">Thêm lớp</a>
    <table>
        <tr>
            <th>Mã</th>
            <th>Tên</th>
            <th></th>
        </tr>
        @foreach ($listGrade as $grade)
            <tr>
                <td>{{ $grade->idGrade }}</td>
                <td>{{ $grade->nameGrade }}</td>
            </tr>
        @endforeach
    </table>
    {{ $listGrade->links() }}
</body>

</html>
