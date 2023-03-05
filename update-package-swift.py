#!/usr/bin/env python3
import glob

def main():
    
    resources = ""
    filenames = globs([
        "**/*.tif",
        "**/*.json",
        "**/DK",
        "**/FO",
        "**/ISL",
        "**/NKG",
        "proj.db",
        "proj.ini"
    ])
    filenames += "proj.db"
    filenames += "proj.ini"
    for filename in filenames:
        if "/" not in filename and filename != "proj.db" and filename != "proj.ini":
            continue
        resources += '                .process("{}"),\n'.format(filename)
    package_swift = template.strip().replace("{resources}", resources.rstrip())
    with open("Package.swift", "w") as file:
        file.write(package_swift)

def globs(pathnames):
    output = []
    for pathname in pathnames:
        output += glob.glob(pathname, recursive=True)
    return sorted(list(dict.fromkeys(output)))

template = """
// swift-tools-version: 5.7
import PackageDescription

let package = Package(
    name: "ProjSwiftData",
    products: [
        .library(
            name: "ProjSwiftData",
            targets: [
                "ProjSwiftData"
            ])
    ],
    dependencies: [],
    targets: [
        .target(
            name: "ProjSwiftData",
            dependencies: [],
            path: "",
            sources: [
                "ProjSwiftData.swift"
            ],
            resources: [
{resources}
            ]),
    ]
)
"""

if __name__ == "__main__":
    main()
