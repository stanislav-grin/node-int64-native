{
  "targets": [
    {
      "target_name": "Int64",
      "sources": [
        "src/main.cpp",
        "src/Int64.cpp"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
    }
  ]
}
