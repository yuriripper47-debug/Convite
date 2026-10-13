from pathlib import Path

ROOT = Path(__file__).resolve().parent
CREATURES = ROOT / 'assets' / 'creatures'
CREATURES.mkdir(parents=True, exist_ok=True)


def write_svg(name: str, svg: str):
    (CREATURES / name).write_text(svg, encoding='utf-8')


write_svg('crab.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240">
  <g stroke="#c75f2a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M68 90c-18-18-21-45-8-62 18-23 52-29 78-13 25 15 32 46 18 71-13 23-31 31-54 31-14 0-26-8-34-27Z" fill="#f7b68a"/>
    <path d="M248 90c18-18 21-45 8-62-18-23-52-29-78-13-25 15-32 46-18 71 13 23 31 31 54 31 14 0 26-8 34-27Z" fill="#f7b68a"/>
    <path d="M92 95c-15 13-25 34-25 58 0 39 27 71 62 71h22c35 0 62-32 62-71 0-23-10-44-24-58l-20 13c-8 5-17 8-27 8-10 0-19-3-27-8l-23-13Z" fill="#f8a66d"/>
    <path d="M89 111c-11 7-18 20-20 34" fill="none"/>
    <path d="M229 111c11 7 18 20 20 34" fill="none"/>
    <g fill="#fff6eb">
      <circle cx="130" cy="124" r="10"/>
      <circle cx="190" cy="124" r="10"/>
    </g>
    <g fill="#2f2b28">
      <circle cx="130" cy="124" r="4"/>
      <circle cx="190" cy="124" r="4"/>
    </g>
    <path d="M148 147c8 9 16 13 24 13s16-4 24-13" fill="none"/>
    <path d="M103 166c-18 12-34 33-35 49" fill="none"/>
    <path d="M216 166c18 12 34 33 35 49" fill="none"/>
    <path d="M132 177c-12 12-19 25-20 38" fill="none"/>
    <path d="M188 177c12 12 19 25 20 38" fill="none"/>
    <g fill="#f5b07f">
      <path d="M80 108c-18 8-31 24-34 42 8 4 19 3 29-2 12-7 19-18 22-35l-17-5Z"/>
      <path d="M240 108c18 8 31 24 34 42-8 4-19 3-29-2-12-7-19-18-22-35l17-5Z"/>
    </g>
  </g>
</svg>
''')


write_svg('turtle.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 260">
  <g stroke="#5ca174" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M82 117c0-42 32-76 75-76h42c42 0 75 34 75 76v14c0 50-40 90-90 90h-18c-50 0-90-40-90-90v-14Z" fill="#b9dcb4"/>
    <path d="M97 123c18-25 56-42 95-42 42 0 76 18 97 57l-30 21c-13 9-28 14-45 14-33 0-61-11-84-33l-33-17Z" fill="#d7efd5"/>
    <path d="M149 89l-29 12-24-37 24-16 29 41Z" fill="#cfeac7"/>
    <path d="M211 89l29 12 24-37-24-16-29 41Z" fill="#cfeac7"/>
    <path d="M135 84c14-20 35-35 59-35 25 0 47 13 63 35" fill="none"/>
    <g fill="#fffaf3">
      <circle cx="150" cy="143" r="8"/>
      <circle cx="210" cy="143" r="8"/>
    </g>
    <g fill="#3a3b3d">
      <circle cx="150" cy="143" r="3.5"/>
      <circle cx="210" cy="143" r="3.5"/>
    </g>
    <path d="M164 168c8 9 15 13 23 13s15-4 23-13" fill="none"/>
    <path d="M90 171c-17 15-34 26-53 30" fill="none"/>
    <path d="M270 171c17 15 34 26 53 30" fill="none"/>
    <path d="M102 148c-17-9-29-12-41-13" fill="none"/>
    <path d="M258 148c17-9 29-12 41-13" fill="none"/>
  </g>
</svg>
''')


write_svg('octopus.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 250">
  <g stroke="#7869a2" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M102 90c-17-25-13-57 14-77 32-24 88-22 120 1 29 21 37 54 20 82l-28 45c-11 18-24 32-41 41-17 9-36 9-51 0-18-10-33-24-45-42l-29-50Z" fill="#c5bfe6"/>
    <path d="M90 103c-19 3-35 18-42 36-9 21 0 42 19 53 18 10 37 11 58 4-6-26-15-53-35-93Z" fill="#c9c4ef"/>
    <path d="M247 103c19 3 35 18 42 36 9 21 0 42-19 53-18 10-37 11-58 4 6-26 15-53 35-93Z" fill="#c9c4ef"/>
    <path d="M112 150c-12 27-14 57-5 82 19 1 41-6 54-23 9-12 15-27 17-44-18 0-36-8-66-15Z" fill="#c9c4ef"/>
    <path d="M227 150c12 27 14 57 5 82-19 1-41-6-54-23-9-12-15-27-17-44 18 0 36-8 66-15Z" fill="#c9c4ef"/>
    <g fill="#fffdfb">
      <circle cx="137" cy="115" r="8"/>
      <circle cx="203" cy="115" r="8"/>
    </g>
    <g fill="#2c2e36">
      <circle cx="137" cy="115" r="3.5"/>
      <circle cx="203" cy="115" r="3.5"/>
    </g>
    <path d="M160 141c10 8 19 12 28 12 9 0 18-4 28-12" fill="none"/>
    <path d="M134 176c10 11 20 16 31 16 12 0 22-5 31-16" fill="none"/>
    <path d="M128 83c-9-16-20-28-32-36" fill="none"/>
    <path d="M210 83c9-16 20-28 32-36" fill="none"/>
    <path d="M117 56c-4-18-1-31 11-44" fill="none"/>
    <path d="M221 56c4-18 1-31-11-44" fill="none"/>
  </g>
</svg>
''')


write_svg('whale.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 260">
  <g stroke="#5e8aa6" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M71 141c0-29 24-53 54-53h108c34 0 62 27 62 60v17c0 32-26 58-58 58H127c-31 0-56-25-56-56v-26Z" fill="#bfe0f1"/>
    <path d="M182 84c15-25 43-38 76-35-14 18-19 38-11 56 10 25 29 35 53 40-30 4-59-4-90-23l-28-38Z" fill="#aed0e6"/>
    <path d="M72 148c-27 2-47 18-60 46 20-4 40-6 56-6 17 0 34 3 52 9-15-22-26-38-48-49Z" fill="#c9e3f4"/>
    <g fill="#fffdf9">
      <circle cx="151" cy="140" r="7"/>
      <circle cx="196" cy="140" r="7"/>
    </g>
    <g fill="#2d3240">
      <circle cx="151" cy="140" r="3.5"/>
      <circle cx="196" cy="140" r="3.5"/>
    </g>
    <path d="M173 171c7 8 14 12 22 12 8 0 15-4 22-12" fill="none"/>
  </g>
</svg>
''')


write_svg('seahorse.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 260">
  <g stroke="#9e7b58" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M102 87c20-31 52-48 85-39 18 5 31 18 38 34 12 27 8 62-17 84-24 21-58 31-90 24-18-4-31-16-40-31-12-22-8-48 24-72Z" fill="#f6d8b0"/>
    <path d="M161 114c42 3 73 26 83 57-13 20-36 31-69 31-29 0-52-9-66-27 20-24 32-45 52-61Z" fill="#f7e4c7"/>
    <path d="M118 141c-17 12-29 30-29 48 0 17 10 33 29 44" fill="none"/>
    <path d="M179 146c17 17 28 36 36 57" fill="none"/>
    <g fill="#f8fbff">
      <circle cx="151" cy="123" r="8"/>
    </g>
    <g fill="#2d2d2d">
      <circle cx="151" cy="123" r="3.5"/>
    </g>
    <path d="M145 166c8 7 15 10 23 10 9 0 15-3 23-10" fill="none"/>
    <path d="M191 77c17-24 31-34 48-40" fill="none"/>
  </g>
</svg>
''')


write_svg('fish.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 260">
  <g stroke="#5a8fa7" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M90 118c21-30 58-50 103-50 52 0 95 28 121 68-28 41-71 70-121 70-45 0-83-19-103-50l-15-38Z" fill="#bfe9fb"/>
    <path d="M214 88c19-9 40-1 58 15 19 16 27 35 23 53-21 4-45-2-62-16-16-12-25-29-19-52Z" fill="#92d1ee"/>
    <path d="M86 134c-15-12-30-17-45-16 9 15 9 29 0 42 16 0 30-4 45-17Z" fill="#9edaf6"/>
    <g fill="#fffdfb">
      <circle cx="168" cy="118" r="7.5"/>
    </g>
    <g fill="#312b33">
      <circle cx="168" cy="118" r="3.5"/>
    </g>
    <path d="M150 147c7 7 14 10 22 10 8 0 15-3 22-10" fill="none"/>
    <path d="M120 92l-13 20 12 22" fill="none"/>
    <path d="M123 97c18-9 39-15 69-16-21 13-31 24-31 40 0 17 10 29 31 42-34-2-55-14-69-32-9-10-10-23 0-34Z" fill="#f9d8b3"/>
  </g>
</svg>
''')


write_svg('starfish.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260">
  <g stroke="#cc7d42" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M130 24l18 45 47-11 11 47 46 18-46 18-11 47-47-11-18 45-18-45-47 11-11-47-46-18 46-18 11-47 47 11 18-45Z" fill="#f7cb72"/>
    <path d="M117 80c9 18 12 35 12 54 0 19-3 36-12 54" fill="none"/>
    <path d="M143 80c-9 18-12 35-12 54 0 19 3 36 12 54" fill="none"/>
    <g fill="#fffdf8">
      <circle cx="118" cy="122" r="8"/>
      <circle cx="142" cy="122" r="8"/>
    </g>
    <g fill="#2c2d31">
      <circle cx="118" cy="122" r="3.5"/>
      <circle cx="142" cy="122" r="3.5"/>
    </g>
    <path d="M105 152c10 11 22 17 35 17 13 0 25-6 35-17" fill="none"/>
  </g>
</svg>
''')


write_svg('pufferfish.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 260">
  <g stroke="#7aa8c5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M92 92c-23 9-40 31-40 58 0 43 32 77 74 77h59c42 0 74-34 74-77 0-27-17-49-40-58l-11 19c-10 18-29 29-49 29s-39-11-49-29l-18-19Z" fill="#bfe0f8"/>
    <path d="M122 92c18-23 37-35 64-35 22 0 41 11 59 35" fill="none"/>
    <g fill="#fffdfb">
      <circle cx="134" cy="128" r="8.5"/>
      <circle cx="186" cy="128" r="8.5"/>
    </g>
    <g fill="#2b2d35">
      <circle cx="134" cy="128" r="3.5"/>
      <circle cx="186" cy="128" r="3.5"/>
    </g>
    <path d="M141 156c12 10 20 15 31 15 12 0 20-5 31-15" fill="none"/>
    <path d="M102 78c-8-18-15-27-29-35" fill="none"/>
    <path d="M220 78c8-18 15-27 29-35" fill="none"/>
  </g>
</svg>
''')

print(f'Generated refined SVG creatures in {CREATURES}')
