@component('mail::message')
# Chào các bạn

Nghỉ hè nhớ đi thực tập

{{ $mess }}
{{-- @component('mail::button', ['url' => ''])
    Button Text
@endcomponent --}}

Chào,<br>
{{ config('app.name') }}
@endcomponent
