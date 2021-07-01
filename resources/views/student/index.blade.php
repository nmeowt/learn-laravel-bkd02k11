@extends('layout.app')

@section('title', 'Danh sách sinh viên')

@section('content')
    <div class="card">
        <div class="card-header card-header-icon" data-background-color="rose">
            <i class="material-icons">assignment</i>
        </div>
        <div class="card-content">
            <h4 class="card-title">Danh sách sinh viên</h4>
            <div class="table-responsive">
                <div class="row">
                    <div class="col-md-4">
                        <form action="">
                            Chọn lớp
                            <select name="id-grade">
                                <option value="">======</option>
                                @foreach ($listGrade as $grade)
                                    <option value="{{ $grade->idGrade }}" @if ($grade->idGrade == $idGrade) selected @endif>
                                        {{ $grade->nameGrade }}
                                    </option>
                                @endforeach
                            </select>
                            <button>ok</button>
                        </form>
                    </div>
                    <div class="col-md-4">
                        <form action="">
                            <input type="text" value="{{ $search }}" name="search">
                            <button>Tìm nó</button>
                        </form>
                    </div>
                </div>
                <table class="table">
                    <tr>
                        <th>Mã</th>
                        <th>Họ tên</th>
                        <th>Giới tính</th>
                        <th>Ngày sinh</th>
                        <th>Lớp</th>
                        <th></th>
                        <th></th>
                    </tr>
                    @foreach ($listStudent as $student)
                        <tr>
                            <td>{{ $student->idStudent }}</td>
                            <td>{{ $student->FullName }}</td>
                            <td>{{ $student->GenderName }}</td>
                            <td>{{ $student->birthDate }}</td>
                            <td>{{ $student->nameGrade }}</td>
                            <td><a class="btn btn-sm btn-warning"
                                    href="{{ route('student.edit', $student->idStudent) }}">Sửa</a></td>
                            <td><a class="btn btn-sm btn-danger"
                                    href="{{ route('student.hide', $student->idStudent) }}">Ẩn</a></td>
                        </tr>
                    @endforeach
                </table>
                {{ $listStudent->appends(['search' => $search])->links() }}
            </div>
        </div>
    </div>
@endsection
