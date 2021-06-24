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
    <form action="">
        <input type="text" value="{{ $search }}" name="search">
        <button>Tìm nó</button>
    </form>
    <table>
        <tr>
            <th>Mã</th>
            <th>Tên</th>
            <th></th>
            <th></th>
        </tr>
        @foreach ($listGrade as $grade)
            <tr>
                <td>{{ $grade->idGrade }}</td>
                <td>{{ $grade->nameGrade }}</td>
                <td><a href="{{ route('grade.show', $grade->idGrade) }}">Xem</a></td>
                <td>
                    <form action="{{ route('grade.destroy', $grade->idGrade) }}" method="post">
                        @csrf
                        @method('DELETE')
                        <button>Xóa</button>
                    </form>
                </td>
            </tr>
        @endforeach
    </table>
    {{ $listGrade->appends([
        'search' => $search,
    ])->links() }}
</body>

</html>
