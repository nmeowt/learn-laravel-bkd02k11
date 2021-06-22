<?php

namespace App\Http\Controllers;

class StudentController extends Controller
{
    public function getName($name)
    {
        // return view('student.index', compact('name'));
        return view('student.index', [
            "abc" => $name
        ]);
    }
}
