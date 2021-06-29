@extends('layout.app')

@section('title', 'Danh sách lớp')

@section('content')
    <div class="card">
        <div class="card-header card-header-icon" data-background-color="rose">
            <i class="material-icons">assignment</i>
        </div>
        <div class="card-content">
            <h4 class="card-title">Danh sách lớp</h4>
            <div class="table-responsive">
                <a href="{{ route('grade.create') }}">Thêm lớp</a>
                <form action="">
                    <input type="text" value="{{ $search }}" name="search">
                    <button>Tìm nó</button>
                </form>
                <table class="table">
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
                            <td><a class="btn btn-sm btn-primary"
                                    href="{{ route('grade.show', $grade->idGrade) }}">Xem</a></td>
                            <td><a class="btn btn-sm btn-warning"
                                    href="{{ route('grade.edit', $grade->idGrade) }}">Sửa</a></td>
                            <td>
                                <form action="{{ route('grade.destroy', $grade->idGrade) }}" method="post">
                                    @csrf
                                    @method('DELETE')
                                    <button class="btn btn-sm btn-danger">Xóa</button>
                                </form>
                            </td>
                        </tr>
                    @endforeach
                </table>
                {{ $listGrade->appends([
        'search' => $search,
    ])->links() }}
            </div>
        </div>
    </div>
@endsection
