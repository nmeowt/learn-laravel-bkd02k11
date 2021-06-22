<?php

namespace App\Http\Controllers;

use App\Models\Grade;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class GradeController extends Controller
{
    public function create()
    {
        return view('grade.create');
    }

    public function store(Request $req)
    {
        $name = $req->get('name');
        // ORM => Eloquent
        $grade = new Grade();
        $grade->nameGrade = $name;
        $grade->save();

        // Query raw
        // DB::insert('insert into grade(nameGrade) values (?), [
        //     $name
        // ]');
        // Query builder
        // DB::table("grade")->insert([
        //     "nameGrade" => $name,
        // ]);
    }
}
