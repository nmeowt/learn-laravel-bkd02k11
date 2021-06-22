<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <h1>Cách cũ: <?php echo $abc; ?> <br> Cách mới: {{ $abc }} </h1>
    <?php
    $a = 5;
    echo $a;
    ?>
    @php
        $a = 5;
        echo $a;
    @endphp
    {{-- Vòng lặp foreach --}}
    {{-- <?php foreach ($iterable as $item):
        # code...
    endforeach; ?>

    @foreach ($collection as $item)

    @endforeach

    @for ($i = 0; $i < $count; $i++)
        
    @endfor --}}

    @if ($a == 5)
        <h1>oooooo</h1>
    @endif


</body>

</html>
