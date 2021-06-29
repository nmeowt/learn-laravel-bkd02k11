@extends('layout.app')

@section('title', 'Thêm lớp')

@section('content')
    <h1>Thêm lớp nè</h1>
    <form action="{{ route('grade.store') }}" method="post">
        @csrf
        Tên: <input type="text" name="name" required> <br>
        <button>Ok</button>
    </form>
@endsection
