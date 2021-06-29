@extends('layout.app')
@section('title', 'Cập nhật lớp')
@section('content')
    <h1>Sửa lớp đó</h1>
    <form action="{{ route('grade.update', $grade->idGrade) }}" method="post">
        @method('PUT')
        @csrf
        Tên: <input type="text" name="z" value="{{ $grade->nameGrade }}">
        <br>
        <button>Cập nhật</button>
    </form>
@endsection
