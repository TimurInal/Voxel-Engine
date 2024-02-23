#version 330 core

layout (location = 0) out vec4 fragColour;

uniform vec3 lightColour;
in vec3 colour;

void main() {
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColour;

    vec3 result = ambient * colour;
    fragColour = vec4(result, 1.0);
}